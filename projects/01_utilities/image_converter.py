import os
from PIL import Image

def resize_by_cm_and_kb(image_path, output_path, target_cm_w, target_cm_h, target_dpi, target_kb):
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    img = Image.open(image_path)
    if img.mode in ('RGBA', 'LA'):
        img = img.convert('RGB')

    target_bytes = target_kb * 1024

    # 1. Convert Centimeters to Pixels using the DPI
    # Formula: (cm / 2.54) * DPI
    pixel_w = int((target_cm_w / 2.54) * target_dpi)
    pixel_h = int((target_cm_h / 2.54) * target_dpi)
    
    print(f"\nConverting {target_cm_w}cm x {target_cm_h}cm at {target_dpi} DPI...")
    print(f"Target pixel dimensions: {pixel_w}x{pixel_h} px")

    # 2. Resize the image to the exact pixel dimensions requested
    # We use LANCZOS resampling to keep the image as sharp/unblurred as possible
    img = img.resize((pixel_w, pixel_h), Image.Resampling.LANCZOS)

    # 3. Binary Search for the best JPEG quality to hit the KB target
    low, high = 1, 95
    best_quality = 75
    
    while low <= high:
        mid = (low + high) // 2
        img.save(output_path, "JPEG", dpi=(target_dpi, target_dpi), quality=mid)
        current_size = os.path.getsize(output_path)
        
        if current_size <= target_bytes:
            best_quality = mid
            low = mid + 1
        else:
            high = mid - 1

    # 4. Final Save
    img.save(output_path, "JPEG", dpi=(target_dpi, target_dpi), quality=best_quality)
    
    final_size_kb = os.path.getsize(output_path) / 1024
    print("\n--- Process Complete ---")
    print(f"Output saved to: {output_path}")
    print(f"Final Physical Size: {target_cm_w}cm x {target_cm_h}cm")
    print(f"Final Pixel Size: {pixel_w}x{pixel_h} px")
    print(f"Final File Size: {final_size_kb:.2f} KB (JPEG Quality: {best_quality})")

    # Guardrail check
    if final_size_kb > target_kb:
        print("\n> [Warning]: Even at lowest quality, the dimensions are too large for a 20KB file.")
        print("> To fix this, you will either need to reduce the target cm dimensions or lower the DPI (e.g., to 150 or 200).")

if __name__ == "__main__":
    # User Inputs
    img_input = input("Enter photo path: ").strip()
    
    try:
        cm_w = float(input("Enter target Width in cm (e.g., 3.5 for passport): "))
        cm_h = float(input("Enter target Height in cm (e.g., 4.5 for passport): "))
        dpi_input = int(input("Enter DPI (e.g., 300): "))
        kb_input = int(input("Enter max KB (e.g., 20): "))
    except ValueError:
        print("Error: Please enter valid numbers for dimensions, DPI, and KB.")
        exit()

    # Create output path
    dir_name, file_name = os.path.split(img_input)
    name, _ = os.path.splitext(file_name)
    img_output = os.path.join(dir_name, f"{name}_{cm_w}x{cm_h}cm.jpg")

    # Run execution
    resize_by_cm_and_kb(img_input, img_output, cm_w, cm_h, dpi_input, kb_input)