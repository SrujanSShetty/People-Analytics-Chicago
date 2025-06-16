# 👥 People Analytics Chicago – Community Dashboard

> **A tribute to the People Analytics Chicago community, built with a full ETL pipeline and visualized through Looker Studio.**

## 📌 Project Overview

On **May 20, 2025**, I attended one of my favorite meetups — the *People Analytics Chicago* session on **AI in People Analytics**, which also served as a heartfelt farewell to **Chris Broderick**, whose leadership has inspired a vibrant and passionate community.

As a token of appreciation, I built this **interactive community dashboard** — hosted on a custom **Google Site**, powered by a complete **ETL pipeline**, and designed to reflect the **talent, diversity, and curiosity** of this amazing network.

## 🔗 Live Dashboard

**👉 Open in Google Chrome Desktop (logged into a Google account for full access):**  
[https://lnkd.in/gh2sxqZ3](https://lnkd.in/gh2sxqZ3)

⚠️ *Note: Embedded Looker Studio dashboards may not load properly on Safari or non-Chrome browsers.*

## 📂 GitHub Repository Contents

This repository contains the **code, enriched data, and build process** used to develop the dashboard, including:

- Python scripts for data cleaning & enrichment
- Excel files for transformation logic
- Sketches and early design files
- JSON or embed code for Google Sites integration
- Documentation of the ETL workflow

---

## 🧱 Tech Stack

| Stage         | Tools Used                                             |
|---------------|--------------------------------------------------------|
| **Extract**   | [PhantomBuster](https://phantombuster.com/) – for scraping public LinkedIn data |
| **Transform** | Python (Pandas), Excel (Power Query), [OpenAI](https://platform.openai.com) – for enrichment and cleansing |
| **Load**      | [Looker Studio](https://lookerstudio.google.com/) – for visualization |
| **Hosting**   | [Google Sites](https://sites.google.com) – to embed and present the dashboard |
| **Prototyping** | Pencil & Paper, HTML/CSS/JS (initial drafts) |

---

## 🔄 ETL Pipeline Overview

1. **Extract**  
   - Used PhantomBuster’s LinkedIn Phantom to extract public profile data (names, roles, locations, etc.) from the People Analytics Chicago community.

2. **Transform**  
   - Cleaned and deduplicated data using **Pandas (Python)** and **Excel Power Query**.
   - Applied **OpenAI APIs** to enhance insights (e.g., gender inference, job role clustering, etc.).
   - Structured the final dataset for easy visual storytelling.

3. **Load**  
   - Uploaded the processed dataset to Google Sheets / Looker Studio.
   - Built dynamic visuals (maps, gender balance, job trends, etc.).
   - Embedded the final dashboard in a custom **Google Site**.

---

## 🎨 From Sketch to Studio

The idea hit me *at the event itself*. I came home, grabbed a pencil, and sketched the dashboard I wished existed.  
I first built a basic **HTML/CSS/JS** site and tried embedding a **Power BI** dashboard with a chatbot — but ran into org-level restrictions.  

So I pivoted.

I explored **Looker Studio** — easier to share, Google-native, and exciting to learn. The project came together with the right tools, and a story worth telling.

---

## 📸 Screenshots

*(Add images or dashboard previews here if you like)*  
Example:  
![Dashboard Screenshot](images/dashboard-preview.png)

---

## ⚠️ Data Disclaimer

All data used in this project was **publicly available** via LinkedIn and programmatically enhanced for analytical purposes only.  
If any information appears incorrect or misrepresented, please feel free to contact me — I’ll correct or remove it immediately.

---

## 💛 Acknowledgments

- Special thanks to **Chris Broderick** for her leadership and inspiration.
- The entire **People Analytics Chicago** community — this wouldn’t exist without your energy and spirit.

**This one’s for you.**

---

## 🧠 Learn More

- [PhantomBuster Documentation](https://hub.phantom.app)
- [Looker Studio Guide](https://support.google.com/looker-studio)
- [OpenAI API](https://platform.openai.com/docs)

---

## 📫 Contact

Feel free to connect with me:  
[LinkedIn](https://linkedin.com/in/srujanshekar) | [GitHub](https://github.com/srujanshetty)

---

## 📌 Tags

`#PeopleAnalytics` `#ETL` `#AI` `#LookerStudio` `#OpenAI` `#GoogleSites` `#DataStorytelling` `#CommunityDriven` `#Python` `#Excel` `#PhantomBuster`
