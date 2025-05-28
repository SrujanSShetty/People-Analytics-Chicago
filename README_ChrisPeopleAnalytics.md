
# Chris's People Analytics AI Dashboard

## 🚀 Overview
This project is a full-stack, cost-effective AI-powered People Analytics Dashboard built for end-users like Chris to explore and gain insights from LinkedIn data using natural language prompts.

Using PhantomBuster for data extraction, Power BI for data visualization, and an embedded chatbot powered by OpenRouter + GPT (OpenAI-compatible), this solution allows a non-technical user to:
- View a live dashboard
- Ask questions using plain English
- Get insights without touching any code

This project is also a tribute to **Chris Broderick**, a highly respected board member of the People Analytics community in Chicago. After her final event on May 20 in Chicago and her transition to Texas, this dashboard honors her invaluable contributions by showcasing the vibrant community she helped shape. 

---

## 🎯 Dashboard Features
Chris can interact with a rich and dynamic dashboard that offers:
- **Field-Wise Breakdown:** Visualize the diversity of domains (HR, Tech, Marketing, etc.) in the community
- **Years of Experience Filters:** See talent distribution by industry veterans vs early-career professionals
- **Age Segmentation:** (if included in dataset) Understand generational diversity in the network
- **Designation Distribution:** From interns to CXOs, discover the hierarchy and roles
- **Location Mapping:** Geospatial view of members across cities, highlighting the Chicago core
- **Live Q&A with AI Assistant:** Simply ask, "Who are the data scientists in New York with 5+ years of experience?"
- **Interactive Visual Insights:** Drill-down options, slicers, and page navigation
- **Sentiment or Engagement Heatmaps:** (Future version) Discover who’s active and engaged online
- **Smart Suggestions:** AI recommends follow-up questions to ask the dashboard

This is not just a dashboard — it’s a digital monument to the People Analytics community and a respectful nod to Chris’s inspiring leadership.

---

## 📥 Step-by-Step Workflow

### 1. **Data Collection using PhantomBuster**
- **Tool Used:** [PhantomBuster](https://phantombuster.com)
- **Purpose:** Extract LinkedIn profiles
- **Limitation:** Free version allows 10 rows per CSV export
- **Process:**
  - Ran the LinkedIn automation phantom
  - Exported 27 CSV files manually (10 rows each, final one had 1 row)
  - Merged them using Excel or Python
  - Cleaned intermediate "Buy Premium" messages manually or with code

### 2. **Data Cleaning**
- **Tools Considered:** Excel, Python, or Snowflake (Free tier)
- **Actual Approach:**
  - Used Excel/Python to clean garbage rows between file merges
  - Removed "Buy Premium" rows using filtering logic

---

### 3. **Data Visualization in Power BI**
- **Platform:** [Power BI Desktop](https://powerbi.microsoft.com/desktop)
- **Steps Taken:**
  - Imported cleaned CSV into Power BI
  - Created visuals such as:
    - People by Location (Map)
    - Years of Experience (Bar Chart)
    - Industry Breakdown (Pie Chart)
  - Designed user-friendly default dashboard

---

### 4. **Building the AI Chatbot Interface**
- **Tech Used:** HTML + CSS + JavaScript + OpenRouter API
- **Key Features:**
  - Embedded Power BI report
  - Input box to ask questions
  - Button triggers OpenAI-compatible API call
  - Returns human-readable Power BI Q&A query

#### 💡 Example Prompt:
**User:** "Show me people from Chicago with more than 5 years of experience"  
**AI Response:** "People located in Chicago with experience greater than 5 years"

User pastes that into the Power BI Q&A visual — insight in seconds!

---

## 🔧 Setup Instructions

### ✅ Embed Power BI Report
1. Publish your report to Power BI Service
2. Click **File → Embed Report → Website or portal**
3. Copy the embed URL into the iframe:
```html
<iframe src="YOUR_POWER_BI_EMBED_LINK_HERE"></iframe>
```

### ✅ Get Free OpenRouter API Key
1. Go to [https://openrouter.ai](https://openrouter.ai)
2. Sign up and get an API Key
3. Add it in the script:
```js
"Authorization": "Bearer YOUR_OPENROUTER_API_KEY"
```

### ✅ Host the Site (Free Options)
- [GitHub Pages](https://pages.github.com)
- [Netlify](https://www.netlify.com)
- [Vercel](https://vercel.com)

---

## 🧠 Tech Stack Summary
| Component     | Tool / Tech        |
|---------------|--------------------|
| Data Pull     | PhantomBuster      |
| Data Cleaning | Excel / Python     |
| Data Storage  | CSV File           |
| Visualization | Power BI           |
| Chatbot       | OpenRouter + GPT   |
| Front-End     | HTML + CSS + JS    |
| Hosting       | GitHub Pages       |

---

## 🙋‍♀️ Why This Project?
Chris (our user) needed an intuitive way to:
- See her network’s analytics
- Ask questions using natural language
- Avoid tech-heavy interfaces

This project is built for recent grads or bootstrapped startups looking to impress stakeholders with minimal budget 💸 and maximum impact 💥.

It also stands as a tribute to the Chicago People Analytics community and its legacy.

---

## ✨ Future Improvements
- Add Google Sheets live sync
- Use Python/Flask backend for dynamic Power BI filters
- Switch to Azure OpenAI for secure enterprise deployments
- Auto-publish reports using Power BI REST API

---

## 🙌 Credits
- **Built by:** [Your Name Here]
- **Inspired by:** Chris's real-life use case
- **Powered by:** PhantomBuster, Power BI, OpenRouter, and OpenAI

---

## 📸 Screenshots (To Add)
- Dashboard view
- Example chatbot interaction
- Embedded page UI
