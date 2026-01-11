# Frontend Customization Guide for ArtFlow

## Overview

The ArtFlow frontend is built using **Lovable** and deployed as a React/TypeScript application. This guide covers how to customize, extend, and maintain the frontend interface.

**Live Frontend:** https://print-perfection-bot.lovable.app

## Table of Contents
1. [Project Structure](#project-structure)
2. 2. [Getting Started](#getting-started)
   3. 3. [Core Components](#core-components)
      4. 4. [Styling & Theming](#styling--theming)
         5. 5. [API Integration](#api-integration)
            6. 6. [Adding New Pages](#adding-new-pages)
               7. 7. [Customization Examples](#customization-examples)
                  8. 8. [Deployment](#deployment)
                     9. 9. [Troubleshooting](#troubleshooting)
                       
                        10. ---
                       
                        11. ## Project Structure
                       
                        12. ```
                            ArtFlow Frontend (Lovable)
                            ├── src/
                            │   ├── components/          # React components
                            │   │   ├── Sidebar.tsx     # Navigation sidebar
                            │   │   ├── Header.tsx      # Top header bar
                            │   │   └── Dashboard.tsx   # Dashboard page
                            │   ├── pages/               # Page components
                            │   │   ├── Dashboard.tsx
                            │   │   ├── ArtGallery.tsx
                            │   │   ├── BundleGenerator.tsx
                            │   │   ├── Listings.tsx
                            │   │   ├── Orders.tsx
                            │   │   ├── Analytics.tsx
                            │   │   └── Settings.tsx
                            │   ├── services/            # API and service layer
                            │   │   ├── api.ts          # API client configuration
                            │   │   └── useDashboardData.ts  # Data hooks
                            │   ├── styles/              # Global styles
                            │   │   └── globals.css
                            │   └── Index.tsx           # Main entry point
                            ├── public/                  # Static assets
                            ├── package.json            # Dependencies
                            └── tsconfig.json          # TypeScript config
                            ```

                            ## Getting Started

                            ### Prerequisites
                            - Node.js 16+ and npm/yarn
                            - - Lovable Editor access (for visual editing)
                              - - Backend API running (see SETUP_GUIDE.md)
                               
                                - ### Local Development
                               
                                - 1. **Export from Lovable**
                                  2.    - Open project in Lovable editor
                                        -    - Use "Export" feature to get React/TypeScript code
                                             -    - Extract to local directory
                                              
                                                  - 2. **Install Dependencies**
                                                    3.    ```bash
                                                             npm install
                                                             # or
                                                             yarn install
                                                             ```

                                                          3. **Start Development Server**
                                                          4.    ```bash
                                                                   npm run dev
                                                                   # or
                                                                   yarn dev
                                                                   ```
                                                                   Visit http://localhost:5173

                                                            4. **Build for Production**
                                                            5.    ```bash
                                                                     npm run build
                                                                     npm run preview
                                                                     ```

                                                                  ## Core Components

                                                              ### 1. Sidebar Navigation
                                                      **File:** `src/components/Sidebar.tsx`

                                                    The sidebar provides navigation to all 7 main pages:
                                                    - Dashboard
                                                    - - Art Gallery
                                                      - - Bundle Generator
                                                        - - Listings
                                                          - - Orders
                                                            - - Analytics
                                                              - - Settings
                                                               
                                                                - **Customization:**
                                                                - ```tsx
                                                                  // Add new menu item
                                                                  <li>
                                                                    <a href="#/custom-page">
                                                                      <span className="icon">📋</span>
                                                                      <span>Custom Page</span>
                                                                    </a>
                                                                  </li>
                                                                  ```

                                                                  ### 2. Header Component
                                                                  **File:** `src/components/Header.tsx`

                                                                  Displays branding and user profile information.

                                                                  **Customization Options:**
                                                                  - Change logo/branding
                                                                  - - Add user profile dropdown
                                                                    - - Add search functionality
                                                                     
                                                                      - ### 3. Dashboard Page
                                                                      - **File:** `src/pages/Dashboard.tsx`
                                                                     
                                                                      - Main landing page showing:
                                                                      - - Sales metrics
                                                                        - - Recent artworks
                                                                          - - Bundle generator preview
                                                                            - - Quick actions
                                                                             
                                                                              - **Key Features:**
                                                                              - - API integration with fallback UI
                                                                                - - Refresh button for real-time updates
                                                                                  - - Responsive grid layout
                                                                                   
                                                                                    - ### 4. Data Display Pages
                                                                                    - **Files:** `src/pages/{ArtGallery,Listings,Orders,Analytics}.tsx`
                                                                                   
                                                                                    - Each page follows the same pattern:
                                                                                    - 1. Fetch data from API
                                                                                      2. 2. Display in formatted layout
                                                                                         3. 3. Handle loading/error states
                                                                                            4. 4. Provide search/filter capabilities
                                                                                              
                                                                                               5. ## Styling & Theming
                                                                                              
                                                                                               6. ### Theme Colors
                                                                                               7. The application uses a modern dark theme with:
                                                                                              
                                                                                               8. ```css
                                                                                                  /* Primary Colors */
                                                                                                  --primary: #f59e0b      /* Amber/Gold */
                                                                                                  --primary-dark: #d97706

                                                                                                  /* Neutral Colors */
                                                                                                  --bg-dark: #1a1a1a
                                                                                                  --bg-medium: #2d2d2d
                                                                                                  --bg-light: #404040
                                                                                                  --text-primary: #ffffff
                                                                                                  --text-secondary: #a0a0a0

                                                                                                  /* Accent Colors */
                                                                                                  --accent: #60a5fa     /* Blue */
                                                                                                  --success: #10b981    /* Green */
                                                                                                  --danger: #ef4444     /* Red */
                                                                                                  ```

                                                                                                  ### Custom Styling

                                                                                                  1. **Global Styles:** `src/styles/globals.css`
                                                                                                  2.    - Base typography
                                                                                                        -    - Color variables
                                                                                                             -    - Utility classes
                                                                                                              
                                                                                                                  - 2. **Component Styles:** Inline or CSS modules
                                                                                                                    3.    - Scoped to components
                                                                                                                          -    - Use CSS variables for consistency
                                                                                                                          
                                                                                                                          3. **Responsive Design**
                                                                                                                          4.    ```css
                                                                                                                                   /* Mobile First Approach */
                                                                                                                                   @media (min-width: 768px) {
                                                                                                                                     /* Tablet styles */
                                                                                                                                   }
                                                                                                                                   @media (min-width: 1024px) {
                                                                                                                                     /* Desktop styles */
                                                                                                                                   }
                                                                                                                                   ```
                                                                                                                                
                                                                                                                                ### Theming Implementation
                                                                                                                            
                                                                                                                            To change the entire color scheme:
                                                                                                                      
                                                                                                                      1. Edit CSS variables in `globals.css`
                                                                                                                      2. 2. Components automatically use new colors
                                                                                                                      3. No changes needed in individual components
                                                                                                                   
                                                                                                                      4. **Example: Dark to Light Theme**
                                                                                                                      5. ```css
                                                                                                                         :root {
                                                                                                                           --bg-dark: #ffffff;
                                                                                                                           --bg-medium: #f5f5f5;
                                                                                                                           --text-primary: #000000;
                                                                                                                           --text-secondary: #666666;
                                                                                                                           /* ... update all colors ... */
                                                                                                                         }
                                                                                                                         ```
                                                                                                                         
                                                                                                                         ## API Integration
                                                                                                                         
                                                                                                                         ### API Service Layer
                                                                                                                         **File:** `src/services/api.ts`
                                                                                                                         
                                                                                                                         Centralized API client with:
                                                                                                                         - Base URL configuration
                                                                                                                         - - Request/response handling
                                                                                                                           - - Error management
                                                                                                                             - - Fallback data
                                                                                                                              
                                                                                                                               - **Configuration:**
                                                                                                                               - ```ts
                                                                                                                                 const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

                                                                                                                                 export const apiClient = {
                                                                                                                                   // API methods
                                                                                                                                 };
                                                                                                                                 ```
                                                                                                                                 
                                                                                                                                 ### Data Hooks
                                                                                                                                 **File:** `src/hooks/useDashboardData.ts`
                                                                                                                                 
                                                                                                                                 Custom React hooks for data fetching:
                                                                                                                                 
                                                                                                                                 ```ts
                                                                                                                                 export const useDashboardData = () => {
                                                                                                                                   const [data, setData] = useState(null);
                                                                                                                                   const [loading, setLoading] = useState(true);
                                                                                                                                   const [error, setError] = useState(null);

                                                                                                                                   useEffect(() => {
                                                                                                                                     fetchDashboardData();
                                                                                                                                   }, []);

                                                                                                                                   return { data, loading, error };
                                                                                                                                 };
                                                                                                                                 ```
                                                                                                                                 
                                                                                                                                 ### Fallback UI Strategy
                                                                                                                                 
                                                                                                                                 If API is unavailable:
                                                                                                                                 1. Component shows sample/cached data
                                                                                                                                 2. 2. "API connection failed" message displayed
                                                                                                                                    3. 3. User can still navigate and interact
                                                                                                                                       4. 4. Refresh button retries API connection
                                                                                                                                         
                                                                                                                                          5. **Implementation:**
                                                                                                                                          6. ```ts
                                                                                                                                             const data = apiData || FALLBACK_DATA;
                                                                                                                                             ```
                                                                                                                                             
                                                                                                                                             ## Adding New Pages
                                                                                                                                             
                                                                                                                                             ### Step 1: Create Page Component
                                                                                                                                             **File:** `src/pages/CustomPage.tsx`
                                                                                                                                             
                                                                                                                                             ```tsx
                                                                                                                                             import React, { useState, useEffect } from 'react';

                                                                                                                                             export const CustomPage: React.FC = () => {
                                                                                                                                               const [data, setData] = useState(null);

                                                                                                                                               useEffect(() => {
                                                                                                                                                 // Fetch data
                                                                                                                                               }, []);

                                                                                                                                               return (
                                                                                                                                                 <div className="page-container">
                                                                                                                                                   <h1>Custom Page Title</h1>
                                                                                                                                                   {/* Page content */}
                                                                                                                                                 </div>
                                                                                                                                               );
                                                                                                                                             };
                                                                                                                                             ```
                                                                                                                                             
                                                                                                                                             ### Step 2: Add Route
                                                                                                                                             **File:** `src/Index.tsx`
                                                                                                                                             
                                                                                                                                             ```tsx
                                                                                                                                             import { CustomPage } from './pages/CustomPage';

                                                                                                                                             <Route path="/custom-page" component={CustomPage} />
                                                                                                                                             ```
                                                                                                                                             
                                                                                                                                             ### Step 3: Add Navigation Item
                                                                                                                                             **File:** `src/components/Sidebar.tsx`
                                                                                                                                             
                                                                                                                                             ```tsx
                                                                                                                                             <li>
                                                                                                                                               <a href="#/custom-page">
                                                                                                                                                 <span className="icon">🎯</span>
                                                                                                                                                 <span>Custom Page</span>
                                                                                                                                               </a>
                                                                                                                                             </li>
                                                                                                                                             ```
                                                                                                                                             
                                                                                                                                             ### Step 4: Style the Page
                                                                                                                                             Add CSS in globals.css or create component-specific styles:
                                                                                                                                             
                                                                                                                                             ```css
                                                                                                                                             .custom-page-container {
                                                                                                                                               padding: 2rem;
                                                                                                                                               display: grid;
                                                                                                                                               grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                                                                                                                                               gap: 2rem;
                                                                                                                                             }
                                                                                                                                             ```
                                                                                                                                             
                                                                                                                                             ## Customization Examples
                                                                                                                                             
                                                                                                                                             ### Example 1: Change Brand Colors
                                                                                                                                             1. Open `src/styles/globals.css`
                                                                                                                                             2. 2. Update color variables
                                                                                                                                                3. 3. Rebuild and deploy
                                                                                                                                                  
                                                                                                                                                   4. ### Example 2: Add Analytics Tracking
                                                                                                                                                   5. ```tsx
                                                                                                                                                      import { trackEvent } from './services/analytics';

                                                                                                                                                      // In component
                                                                                                                                                      <button onClick={() => {
                                                                                                                                                        trackEvent('button_click', { page: 'dashboard' });
                                                                                                                                                      }}>
                                                                                                                                                        Click Me
                                                                                                                                                        </button>
                                                                                                                                                      ```
                                                                                                                                                      
                                                                                                                                                      ### Example 3: Custom Dashboard Widget
                                                                                                                                                      ```tsx
                                                                                                                                                      // src/components/CustomWidget.tsx
                                                                                                                                                      export const CustomWidget = ({ title, children }) => {
                                                                                                                                                        return (
                                                                                                                                                          <div className="widget">
                                                                                                                                                            <h3>{title}</h3>
                                                                                                                                                                  <div className="widget-content">{children}</div>
                                                                                                                                                          </div>
                                                                                                                                                            );
                                                                                                                                                      };

                                                                                                                                                      // Use in Dashboard
                                                                                                                                                      <CustomWidget title="New Widget">
                                                                                                                                                        {/* Content */}
                                                                                                                                                      </CustomWidget>
                                                                                                                                                      ```
                                                                                                                                                      
                                                                                                                                                      ## Deployment
                                                                                                                                                      
                                                                                                                                                      ### Lovable Deployment
                                                                                                                                                      1. Make changes in Lovable visual editor
                                                                                                                                                      2. Test in preview
                                                                                                                                                      3. Click "Publish" to deploy to live URL
                                                                                                                                                      4. Changes go live immediately
                                                                                                                                                     
                                                                                                                                                      5. ### Self-Hosted Deployment
                                                                                                                                                     
                                                                                                                                                      6. **Build:**
                                                                                                                                                      ```bash
                                                                                                                                                      npm run build
                                                                                                                                                      ```
                                                                                                                                                      
                                                                                                                                                      **Deploy to Vercel:**
                                                                                                                                                      ```bash
                                                                                                                                                      vercel deploy --prod
                                                                                                                                                      ```
                                                                                                                                                      
                                                                                                                                                      **Deploy to Netlify:**
                                                                                                                                                      ```bash
                                                                                                                                                      npm run build
                                                                                                                                                      netlify deploy --prod --dir=dist
                                                                                                                                                      ```
                                                                                                                                                      
                                                                                                                                                      **Docker Deployment:**
                                                                                                                                                      ```bash
                                                                                                                                                      docker build -t artflow-frontend .
                                                                                                                                                      docker run -p 3000:3000 artflow-frontend
                                                                                                                                                      ```
                                                                                                                                                      
                                                                                                                                                      ### Environment Configuration
                                                                                                                                                      Create `.env.production`:
                                                                                                                                                      ```
                                                                                                                                                      VITE_API_URL=https://api.yourdomain.com
                                                                                                                                                      VITE_APP_NAME=ArtFlow
                                                                                                                                                      ```
                                                                                                                                                      
                                                                                                                                                      ## Troubleshooting
                                                                                                                                                      
                                                                                                                                                      ### Common Issues
                                                                                                                                                      
                                                                                                                                                      **1. API Connection Errors**
                                                                                                                                                      - Check backend is running
                                                                                                                                                      - - Verify API_BASE_URL in api.ts
                                                                                                                                                      - Check CORS configuration on backend
                                                                                                                                                      - - Use browser DevTools to debug network requests
                                                                                                                                                       
                                                                                                                                                        - **2. Styling Issues**
                                                                                                                                                        - - Clear browser cache (Ctrl+Shift+Delete)
                                                                                                                                                        - Check CSS variable values
                                                                                                                                                        - - Verify responsive breakpoints
                                                                                                                                                          - - Use browser DevTools to inspect elements
                                                                                                                                                          
                                                                                                                                                          **3. Component Not Rendering**
                                                                                                                                                          - Check console for JavaScript errors
                                                                                                                                                          - - Verify component import paths
                                                                                                                                                            - - Check prop types match interface
                                                                                                                                                            - Ensure state is initialized properly
                                                                                                                                                            
                                                                                                                                                            **4. Build Failures**
                                                                                                                                                            - Clear node_modules: `rm -rf node_modules && npm install`
                                                                                                                                                            - Check TypeScript errors: `npm run type-check`
                                                                                                                                                            - Verify all imports are correct
                                                                                                                                                            - - Check for circular dependencies
                                                                                                                                                            
                                                                                                                                                            ### Debug Mode
                                                                                                                                                            
                                                                                                                                                            Enable detailed logging:
                                                                                                                                                            ```ts
                                                                                                                                                            // In api.ts
                                                                                                                                                            const DEBUG = true;
                                                                                                                                                            if (DEBUG) console.log('API Call:', endpoint, data);
                                                                                                                                                            ```
                                                                                                                                                            
                                                                                                                                                            ## Performance Optimization
                                                                                                                                                            
                                                                                                                                                            ### Code Splitting
                                                                                                                                                            ```tsx
                                                                                                                                                            import React, { lazy, Suspense } from 'react';
                                                                                                                                                            
                                                                                                                                                            const Analytics = lazy(() => import('./pages/Analytics'));

                                                                                                                                                            // Use with Suspense
                                                                                                                                                            <Suspense fallback={<Loading />}>
                                                                                                                                                              <Analytics />
                                                                                                                                                            </Suspense>
                                                                                                                                                            ```
                                                                                                                                                            
                                                                                                                                                            ### Image Optimization
                                                                                                                                                            ```tsx
                                                                                                                                                            <img
                                                                                                                                                              src="image.webp" 
                                                                                                                                                                alt="description"
                                                                                                                                                                  loading="lazy"
                                                                                                                                                              width="300"
                                                                                                                                                              height="200"
                                                                                                                                                              />
                                                                                                                                                            ```
                                                                                                                                                            
                                                                                                                                                            ### Memoization
                                                                                                                                                            ```tsx
                                                                                                                                                            import React, { memo } from 'react';
                                                                                                                                                            
                                                                                                                                                            const ExpensiveComponent = memo(({ data }) => {
                                                                                                                                                              return <div>{/* render data */}</div>;
                                                                                                                                                            });
                                                                                                                                                            ```
                                                                                                                                                            
                                                                                                                                                            ## Resources
                                                                                                                                                            
                                                                                                                                                            - **Lovable Docs:** https://lovable.dev/docs
                                                                                                                                                            - **React Docs:** https://react.dev
                                                                                                                                                            - - **TypeScript Docs:** https://www.typescriptlang.org/docs
                                                                                                                                                              - - **CSS-in-JS:** https://styled-components.com
                                                                                                                                                                - - **API Integration:** See API_DOCUMENTATION.md
                                                                                                                                                                 
                                                                                                                                                                  - ## Support
                                                                                                                                                                 
                                                                                                                                                                  - For issues or questions:
                                                                                                                                                                  1. Check the troubleshooting section
                                                                                                                                                                  2. 2. Review existing GitHub issues
                                                                                                                                                                  3. Create a new GitHub issue with details
                                                                                                                                                                  4. Contact the development team
                                                                                                                                                                  
                                                                                                                                                                  ---
                                                                                                                                                                  
                                                                                                                                                                  **Last Updated:** January 11, 2026
                                                                                                                                                                  **Version:** 1.0.0
