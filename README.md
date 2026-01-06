# 🚀 Etsy Print Art Automation System

Fully automated AI-powered system to generate, optimize, and sell print-on-demand art on Etsy and TikTok using OpenAI Agents SDK.

## ✨ Features

- 🎨 **AI Art Generation**: Generate unlimited variations using DALL-E 3
- - 📝 **Smart Listing Creation**: SEO-optimized Etsy listings with descriptions
  - - 📱 **TikTok Integration**: Auto-generate captions and schedule posts
    - - 📊 **Real-time Dashboard**: Monitor all metrics and workflows
      - - ⏰ **Automated Scheduling**: Daily workflow execution
        - - 💾 **Complete Database**: Track all content, sales, and analytics
          - - 🌐 **Web Interface**: Beautiful Flask dashboard
            - - 🐳 **Docker Ready**: One-command deployment
             
              - ## 🎯 What It Does
             
              - ### Phase 1: Niche Research
              - - Analyzes trending niches on Etsy
                - - Compares competition levels
                  - - Identifies underserved markets
                   
                    - ### Phase 2: Image Generation
                    - - Creates 50+ unique variations per niche
                      - - Multiple artistic styles
                        - - 1024x1024 HD quality
                          - - Ready for 300 DPI printing
                           
                            - ### Phase 3: Listing Creation
                            - - Generates SEO-optimized titles
                              - - Creates compelling descriptions
                                - - Assigns relevant tags
                                  - - Sets competitive pricing
                                   
                                    - ### Phase 4: Content Distribution
                                    - - Generates engaging captions
                                      - - Schedules TikTok posts
                                        - - Tracks engagement metrics
                                         
                                          - ## 📊 Architecture
                                         
                                          - ```
                                            OrchestratorAgent
                                            ├── NicheDiscoveryAgent (Market research)
                                            ├── ArtGenerationAgent (DALL-E 3)
                                            ├── ListingManagerAgent (Etsy API)
                                            ├── TikTokManagerAgent (Content scheduling)
                                            └── TaskScheduler (Daily automation)
                                            ```

                                            ## 🚀 Quick Start

                                            ```bash
                                            # 1. Clone repo
                                            git clone https://github.com/kyl3kan3/etsy-automation-agents.git
                                            cd etsy-automation-agents

                                            # 2. Setup environment
                                            cp .env.example .env
                                            # Edit .env with your API keys

                                            # 3. Install dependencies
                                            pip install -r requirements.txt

                                            # 4. Run application
                                            python main.py
                                            ```

                                            Open your browser: `http://localhost:5000`

                                            ## 💻 Technology Stack

                                            - **Backend**: Python, Flask, SQLAlchemy
                                            - - **AI**: OpenAI GPT-4, DALL-E 3
                                              - - **APIs**: Etsy, TikTok
                                                - - **Database**: SQLite (dev), PostgreSQL (prod)
                                                  - - **Scheduling**: APScheduler
                                                    - - **Frontend**: HTML5, CSS3, JavaScript
                                                      - - **Deployment**: Docker, Docker Compose
                                                       
                                                        - ## 📁 Project Structure
                                                       
                                                        - ```
                                                          etsy-automation-agents/
                                                          ├── agents/                 # AI agents
                                                          ├── integrations/          # API clients
                                                          ├── database/             # SQLAlchemy models
                                                          ├── dashboard/            # Flask app
                                                          ├── scheduler/            # Task scheduling
                                                          ├── config/               # Settings
                                                          ├── main.py              # Entry point
                                                          └── requirements.txt     # Dependencies
                                                          ```

                                                          ## 📈 Expected Results

                                                          ### First Month
                                                          - 150-300 listings created
                                                          - - 500+ TikTok posts scheduled
                                                            - - $500-$2000 revenue potential
                                                             
                                                              - ## 💰 Costs
                                                             
                                                              - Per daily workflow (50 images, 10 listings):
                                                              - - DALL-E 3: $2.00
                                                                - - GPT-4: $0.50
                                                                  - - **Total: ~$2.50/day (~$75/month)**
                                                                   
                                                                    - **Potential ROI**: $500-$5000+ monthly revenue
                                                                   
                                                                    - ## 🔧 Configuration
                                                                   
                                                                    - All settings in `config/settings.py`:
                                                                    - - API models and endpoints
                                                                      - - Image generation parameters
                                                                        - - Etsy listing defaults
                                                                          - - Database settings
                                                                           
                                                                            - ## 🐛 Troubleshooting
                                                                           
                                                                            - | Issue | Solution |
                                                                            - |-------|----------|
                                                                            - | API errors | Check logs: `tail -f logs/etsy_automation.log` |
                                                                            - | Image generation slow | Check rate limits |
                                                                            - | Etsy upload fails | Verify API key and shop ID |
                                                                           
                                                                            - ## 📚 Documentation
                                                                           
                                                                            - - [DEPLOYMENT.md](DEPLOYMENT.md) - Setup & deployment guide
                                                                              - - [Config Reference](config/settings.py) - Configuration options
                                                                                - - [API Endpoints](dashboard/app.py) - Dashboard API
                                                                                 
                                                                                  - ## 📞 Support
                                                                                 
                                                                                  - For issues:
                                                                                  - 1. Check logs: `logs/etsy_automation.log`
                                                                                    2. 2. Review [DEPLOYMENT.md](DEPLOYMENT.md)
                                                                                       3. 3. Create a GitHub issue
                                                                                         
                                                                                          4. ## 📝 License
                                                                                         
                                                                                          5. MIT License - Feel free to use and modify
                                                                                         
                                                                                          6. ---
                                                                                         
                                                                                          7. Built with ❤️ for print-on-demand automation
