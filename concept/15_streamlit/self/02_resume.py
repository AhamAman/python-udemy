import streamlit as st

st.set_page_config(page_title="Professional Resume", page_icon="💼", layout="wide")

# Main Header Banner Matrix
st.title("Alex Mercer")
st.write("📍 New York, NY | 📧 alex.mercer@email.com | 🌐 [GitHub](https://github.com) | 🔗 [LinkedIn](https://linkedin.com)")

st.write("---")

# Executive Summary Section
st.header("Executive Summary")
st.write("""
Senior Software Engineer with 5+ years of experience specializing in high-throughput data streaming pipelines and asynchronous backend services. Proven track record of optimizing database query plans and reducing network latency overhead metrics.
""")

# Professional Experience Layout Container
st.header("Professional Experience")

# Job 1
st.subheader("Lead Backend Engineer — Nexus Data Systems")
st.write("*January 2024 – Present*")
st.write("""
* Architected a distributed async worker pool that handles over 50,000 tasks/sec.
* Migrated legacy REST infrastructure to an enterprise-grade ASGI framework, dropping server response latency by 35%.
* Supervised a team of 4 junior engineers implementing strict test-driven development methodologies.
""")

# Job 2
st.subheader("Data Infrastructure Engineer — Apex Logistics")
st.write("*June 2021 – December 2023*")
st.write("""
* Designed and maintained robust connection-pooled PostgreSQL database instances.
* Implemented defensive timeout and rate-limiting gates across external API ingestion vectors to prevent service disruptions.
* Automated telemetry ingestion workflows using Python cron matrix clusters.
""")

st.write("---")

# Technical Skills & Education Core Grid
st.header("Technical Mastery Matrix")
st.write("""
| Category | Tools & Technologies |
| :--- | :--- |
| **Backend & Core** | Python, Asyncio, FastAPI, Starlette |
| **Data Systems** | PostgreSQL, asyncpg, Redis, SQLAlchemy |
| **DevOps & Cloud** | Docker, AWS (EC2, S3), CI/CD pipelines |
""")

st.header("Education")
st.subheader("B.S. in Computer Science")
st.write("*University of Engineering Excellence — Class of 2021*")