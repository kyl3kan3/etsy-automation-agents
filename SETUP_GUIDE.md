# 🚀 Etsy Print Art Automation System - SETUP GUIDE

## ✅ PROJECT STATUS
- **Backend**: 100% Complete (All 5 agents + Flask API)
- - **Frontend**: 100% Complete (Vibecode dashboard built)
  - - **Integration**: Ready for API keys and deployment
   
    - ---

    ## 📋 WHAT'S BEEN BUILT

    ### Backend Components
    ✅ **orchestrator.py** - Main workflow coordinator
    ✅ **niche_discovery.py** - GPT-4 market research engine
    ✅ **art_generation.py** - DALL-E 3 image generator
    ✅ **listing_manager.py** - Etsy API integration
    ✅ **tiktok_manager.py** - Social media scheduler
    ✅ **app.py** - Flask REST API with 12 endpoints

    ### Frontend
    ✅ **PrintArt Pro Dashboard** - Built in Vibecode
       - Dark theme with teal/copper accents
       -    - Dashboard, Analytics, Automation monitoring
            -    - Professional, responsive design
             
                 - ---

                 ## 🔑 API KEYS NEEDED

                 ### Required API Keys to Add

                 1. **OpenAI API Key** (CRITICAL)
                 2.    - Needed for: GPT-4, DALL-E 3
                       -    - Get it: https://platform.openai.com/api-keys
                            -    - Add to: `.env` file as `OPENAI_API_KEY`
                                 -    - Cost: Pay-per-use (GPT-4 ~$0.03/1K tokens, DALL-E 3 ~$0.04-0.12/image)
                                  
                                      - 2. **Etsy API Credentials** (REQUIRED)
                                        3.    - Get it: https://www.etsy.com/developers/documentation
                                              -    - Need: App ID, API Key, Shop ID
                                                   -    - Add to: `.env` as `ETSY_API_KEY`, `ETSY_SHOP_ID`
                                                        -    - Rate limit: 10,000 calls/day
                                                         
                                                             - 3. **TikTok API Credentials** (REQUIRED)
                                                               4.    - Get it: https://developers.tiktok.com/
                                                                     -    - Need: Client ID, Client Secret, Access Token
                                                                          -    - Add to: `.env` as `TIKTOK_API_KEY`
                                                                               -    - Requires TikTok Business account
                                                                                
                                                                                    - ---

                                                                                    ## 🛠️ LOCAL INSTALLATION

                                                                                    ### Prerequisites
                                                                                    ```bash
                                                                                    # Python 3.9+
                                                                                    python --version

                                                                                    # pip
                                                                                    pip --version
                                                                                    ```

                                                                                    ### Step 1: Clone Repository
                                                                                    ```bash
                                                                                    git clone https://github.com/kyl3kan3/etsy-automation-agents.git
                                                                                    cd etsy-automation-agents
                                                                                    ```

                                                                                    ### Step 2: Create Virtual Environment
                                                                                    ```bash
                                                                                    # macOS/Linux
                                                                                    python -m venv venv
                                                                                    source venv/bin/activate

                                                                                    # Windows
                                                                                    python -m venv venv
                                                                                    venv\Scripts\activate
                                                                                    ```

                                                                                    ### Step 3: Install Dependencies
                                                                                    ```bash
                                                                                    pip install -r requirements.txt
                                                                                    ```

                                                                                    ### Step 4: Setup Environment Variables
                                                                                    ```bash
                                                                                    # Copy the example file
                                                                                    cp .env.example .env

                                                                                    # Edit .env with your API keys
                                                                                    nano .env  # or use your preferred editor
                                                                                    ```

                                                                                    Add these to `.env`:
                                                                                    ```env
                                                                                    # OpenAI
                                                                                    OPENAI_API_KEY=sk-...

                                                                                    # Etsy
                                                                                    ETSY_API_KEY=your-etsy-api-key
                                                                                    ETSY_SHOP_ID=12345678

                                                                                    # TikTok
                                                                                    TIKTOK_API_KEY=your-tiktok-key

                                                                                    # Flask
                                                                                    FLASK_ENV=development
                                                                                    FLASK_DEBUG=True
                                                                                    ```

                                                                                    ### Step 5: Run Flask Backend
                                                                                    ```bash
                                                                                    python app.py
                                                                                    ```

                                                                                    Backend will start on: **http://localhost:5000**

                                                                                    ### Step 6: Connect Vibecode Frontend
                                                                                    1. Open the Vibecode dashboard (link provided)
                                                                                    2. 2. Update API endpoint in dashboard settings to: `http://localhost:5000`
                                                                                       3. 3. Test connection with "Check Status" button
                                                                                         
                                                                                          4. ---
                                                                                         
                                                                                          5. ## 📡 API ENDPOINTS
                                                                                         
                                                                                          6. All endpoints are at `http://localhost:5000/api/`
                                                                                         
                                                                                          7. ### Workflow Management
                                                                                          8. - `POST /workflow` - Start automation workflow
                                                                                             - - `GET /workflow/history` - Get execution history
                                                                                              
                                                                                               - ### Niche Research
                                                                                               - - `POST /niche/analyze` - Analyze a niche
                                                                                                 - - `GET /trending-niches` - Get trending niches (limit=10)
                                                                                                  
                                                                                                   - ### Image Generation
                                                                                                   - - `POST /images/generate` - Generate art images
                                                                                                    
                                                                                                     - ### Listing Management
                                                                                                     - - `GET /listings` - Get all listings
                                                                                                       - - `POST /listings` - Create new listing
                                                                                                         - - `POST /listings/{id}/publish` - Publish listing
                                                                                                          
                                                                                                           - ### TikTok Management
                                                                                                           - - `GET /tiktok/posts` - Get scheduled posts
                                                                                                             - - `POST /tiktok/posts` - Schedule new post
                                                                                                               - - `POST /tiktok/captions` - Generate captions
                                                                                                                
                                                                                                                 - ### System
                                                                                                                 - - `GET /status` - Get system status
                                                                                                                  
                                                                                                                   - ---
                                                                                                                   
                                                                                                                   ## 🚀 QUICK START WORKFLOW
                                                                                                                   
                                                                                                                   ### 1. Analyze a Niche
                                                                                                                   ```bash
                                                                                                                   curl -X POST http://localhost:5000/api/niche/analyze \
                                                                                                                     -H "Content-Type: application/json" \
                                                                                                                     -d '{"niche": "kawaii cats"}'
                                                                                                                   ```
                                                                                                                   
                                                                                                                   ### 2. Generate Images
                                                                                                                   ```bash
                                                                                                                   curl -X POST http://localhost:5000/api/images/generate \
                                                                                                                     -H "Content-Type: application/json" \
                                                                                                                     -d '{"niche": "kawaii cats", "num_images": 50}'
                                                                                                                     ```
                                                                                                                   
                                                                                                                   ### 3. Create Listings
                                                                                                                   ```bash
                                                                                                                   curl -X POST http://localhost:5000/api/listings \
                                                                                                                     -H "Content-Type: application/json" \
                                                                                                                     -d '{
                                                                                                                       "title": "Kawaii Cats Art Print",
                                                                                                                       "description": "Beautiful print-on-demand art",
                                                                                                                       "price": 19.99,
                                                                                                                       "image_url": "https://...",
                                                                                                                       "tags": ["art", "cats", "cute"]
                                                                                                                     }'
                                                                                                                   ```
                                                                                                                   
                                                                                                                   ### 4. Generate TikTok Captions
                                                                                                                   ```bash
                                                                                                                   curl -X POST http://localhost:5000/api/tiktok/captions \
                                                                                                                     -H "Content-Type: application/json" \
                                                                                                                     -d '{"niche": "kawaii cats", "num_captions": 10}'
                                                                                                                   ```
                                                                                                                   
                                                                                                                   ### 5. Full Workflow
                                                                                                                   ```bash
                                                                                                                   curl -X POST http://localhost:5000/api/workflow \
                                                                                                                     -H "Content-Type: application/json" \
                                                                                                                     -d '{
                                                                                                                       "niche": "kawaii cats",
                                                                                                                       "num_images": 50,
                                                                                                                       "num_listings": 10
                                                                                                                     }'
                                                                                                                   ```
                                                                                                                   
                                                                                                                   ---
                                                                                                                   
                                                                                                                   ## 💻 DEPLOYMENT OPTIONS
                                                                                                                   
                                                                                                                   ### Option 1: Heroku (Easy)
                                                                                                                   ```bash
                                                                                                                   heroku login
                                                                                                                   heroku create your-app-name
                                                                                                                   git push heroku main
                                                                                                                   heroku config:set OPENAI_API_KEY=sk-...
                                                                                                                   heroku open
                                                                                                                   ```
                                                                                                                   
                                                                                                                   ### Option 2: AWS/GCP/Azure (Scalable)
                                                                                                                   - Use gunicorn WSGI server
                                                                                                                   - - Deploy with Docker: `docker build -t etsy-automation .`
                                                                                                                     - - Use RDS for database
                                                                                                                       - - CloudFront for CDN
                                                                                                                        
                                                                                                                         - ### Option 3: PythonAnywhere (Simple)
                                                                                                                         - - Upload repo
                                                                                                                           - - Configure WSGI file
                                                                                                                             - - Set environment variables
                                                                                                                               - - Enable HTTPS
                                                                                                                                
                                                                                                                                 - ---
                                                                                                                                 
                                                                                                                                 ## 🐛 TROUBLESHOOTING
                                                                                                                                 
                                                                                                                                 ### Issue: "OpenAI API key not found"
                                                                                                                                 **Solution**: Check `.env` file has `OPENAI_API_KEY` set correctly
                                                                                                                                 ```bash
                                                                                                                                 echo $OPENAI_API_KEY  # Should print your key
                                                                                                                                 ```
                                                                                                                                 
                                                                                                                                 ### Issue: "ModuleNotFoundError: No module named 'agents'"
                                                                                                                                 **Solution**: Make sure you're in the project root directory
                                                                                                                                 ```bash
                                                                                                                                 pwd  # Should end in /etsy-automation-agents
                                                                                                                                 ```
                                                                                                                                 
                                                                                                                                 ### Issue: "Connection refused" when calling API
                                                                                                                                 **Solution**: Ensure Flask is running
                                                                                                                                 ```bash
                                                                                                                                 python app.py  # Starts on port 5000
                                                                                                                                 ```
                                                                                                                                 
                                                                                                                                 ### Issue: "Rate limit exceeded" from OpenAI
                                                                                                                                 **Solution**: Add delays between requests or upgrade API plan
                                                                                                                                 ```python
                                                                                                                                 import time
                                                                                                                                 time.sleep(1)  # Wait 1 second between calls
                                                                                                                                 ```
                                                                                                                                 
                                                                                                                                 ---
                                                                                                                                 
                                                                                                                                 ## 📊 COST ESTIMATION
                                                                                                                                 
                                                                                                                                 ### Monthly Costs (Moderate Usage)
                                                                                                                                 - **OpenAI GPT-4**: $20-50/month (1000 requests)
                                                                                                                                 - - **DALL-E 3**: $30-100/month (100-300 images)
                                                                                                                                   - - **Etsy API**: FREE (first 10,000 calls/day)
                                                                                                                                   - **TikTok API**: FREE (basic tier)
                                                                                                                                   - - **Hosting**: $5-20/month (Heroku/AWS free tier)
                                                                                                                                    
                                                                                                                                     - **Total**: $50-170/month
                                                                                                                                    
                                                                                                                                     - ### Revenue Potential
                                                                                                                                     - - Average listing price: $17-25
                                                                                                                                       - - Conversion rate: 1-3%
                                                                                                                                         - - 100 listings → $10,000-75,000 monthly potential
                                                                                                                                           - 
                                                                                                                                           ---
                                                                                                                                           
                                                                                                                                           ## ✨ NEXT STEPS
                                                                                                                                           
                                                                                                                                           1. **Get API Keys** (see above)
                                                                                                                                           2. 2. **Run locally** to test
                                                                                                                                              3. 3. **Connect Vibecode frontend**
                                                                                                                                              4. **Deploy to production**
                                                                                                                                              5. 5. **Monitor earnings**
                                                                                                                                                
                                                                                                                                                 6. ---
                                                                                                                                                
                                                                                                                                                 7. ## 📚 DOCUMENTATION
                                                                                                                                                 8. 
                                                                                                                                                 - OpenAI Agents SDK: https://platform.openai.com/docs/guides/agents-sdk
                                                                                                                                                 - Etsy API Docs: https://www.etsy.com/developers/documentation
                                                                                                                                                 - - TikTok API Docs: https://developers.tiktok.com/doc/
                                                                                                                                                   - - Flask Docs: https://flask.palletsprojects.com/
                                                                                                                                                    
                                                                                                                                                     - ---
                                                                                                                                                     
                                                                                                                                                     ## 🆘 SUPPORT
                                                                                                                                                     
                                                                                                                                                     Issues? Check:
                                                                                                                                                     1. Console logs: `logs/etsy_automation.log`
                                                                                                                                                     2. 2. Network tab in browser developer tools
                                                                                                                                                        3. 3. GitHub Issues: https://github.com/kyl3kan3/etsy-automation-agents/issues
                                                                                                                                                           4. 
                                                                                                                                                           ---
                                                                                                                                                           
                                                                                                                                                           ## 📝 License
                                                                                                                                                           MIT License - Free to use and modify
                                                                                                                                                           
                                                                                                                                                           **Built with ❤️ using Claude, OpenAI Agents SDK, and Vibecode**
