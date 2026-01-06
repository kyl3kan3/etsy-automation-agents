"""
Orchestrator Agent - Main coordinator for all automation workflows
Uses OpenAI Agents SDK to coordinate niche discovery, art generation, 
listing creation, and TikTok distribution.
"""

import os
from typing import Optional, Dict, Any
from datetime import datetime
import logging

from openai import OpenAI

logger = logging.getLogger(__name__)


class OrchestratorAgent:
      """
          Main orchestrator that coordinates all agents in the system.
              Manages the workflow: Niche Research -> Art Generation -> Listing Creation -> Content Distribution
                  """

    def __init__(self, api_key: Optional[str] = None):
              """
                      Initialize the Orchestrator Agent.

                                      Args:
                                                  api_key: OpenAI API key. If None, uses OPENAI_API_KEY environment variable.
                                                          """
              self.api_key = api_key or os.getenv("OPENAI_API_KEY")
              if not self.api_key:
                            raise ValueError("OpenAI API key not provided. Set OPENAI_API_KEY environment variable.")

              self.client = OpenAI(api_key=self.api_key)
              self.model = "gpt-4-turbo"
              self.workflow_state = {}
              self.execution_history = []

        logger.info("OrchestratorAgent initialized")

    def run_workflow(self, niche: str, num_images: int = 50, num_listings: int = 10) -> Dict[str, Any]:
              """
                      Run complete automation workflow for a given niche.

                                      Args:
                                                  niche: Target niche for automation (e.g., "kawaii cats", "minimalist furniture")
                                                              num_images: Number of images to generate (default: 50)
                                                                          num_listings: Number of Etsy listings to create (default: 10)

                                                                                              Returns:
                                                                                                          Dict containing workflow results and execution details
                                                                                                                  """
              workflow_id = f"workflow_{datetime.now().isoformat()}"
              logger.info(f"Starting workflow {workflow_id} for niche: {niche}")

        try:
                      # Phase 1: Niche Research
                      logger.info("Phase 1: Analyzing niche market...")
                      niche_analysis = self._analyze_niche(niche)
                      self.workflow_state["niche_analysis"] = niche_analysis

            # Phase 2: Art Generation  
                      logger.info(f"Phase 2: Generating {num_images} unique art variations...")
                      art_generation = self._generate_art(niche, num_images)
                      self.workflow_state["generated_art"] = art_generation

            # Phase 3: Listing Creation
                      logger.info(f"Phase 3: Creating {num_listings} SEO-optimized listings...")
                      listings = self._create_listings(niche, num_listings, art_generation)
                      self.workflow_state["listings"] = listings

            # Phase 4: Content Distribution
                      logger.info("Phase 4: Scheduling TikTok content...")
                      tiktok_schedule = self._schedule_tiktok_content(niche, num_listings)
                      self.workflow_state["tiktok_schedule"] = tiktok_schedule

            result = {
                              "workflow_id": workflow_id,
                              "status": "completed",
                              "niche": niche,
                              "niche_analysis": niche_analysis,
                              "images_generated": len(art_generation.get("images", [])),
                              "listings_created": len(listings.get("listings", [])),
                              "tiktok_posts_scheduled": len(tiktok_schedule.get("posts", [])),
                              "timestamp": datetime.now().isoformat()
            }

            self.execution_history.append(result)
            logger.info(f"Workflow {workflow_id} completed successfully")
            return result

except Exception as e:
            logger.error(f"Workflow {workflow_id} failed: {str(e)}")
            return {
                              "workflow_id": workflow_id,
                              "status": "failed",
                              "error": str(e),
                              "timestamp": datetime.now().isoformat()
            }

    def _analyze_niche(self, niche: str) -> Dict[str, Any]:
              """
                      Use GPT-4 to analyze niche market viability and competition.
                              Delegates to NicheDiscoveryAgent in production.
                                      """
              prompt = f"""Analyze the "{niche}" niche for Etsy print-on-demand products:
              1. Market viability (1-10)
              2. Competition level (low/medium/high)
              3. Top 5 trending variations
              4. Recommended price range
              5. Key keywords for SEO

              Provide structured analysis."""

              try:
                  response = self.client.chat.completions.create(
                      model=self.model,
                      messages=[
                          {"role": "system", "content": "You are a market research expert for Etsy print-on-demand products."},
                          {"role": "user", "content": prompt}
                      ],
                      temperature=0.7,
                      max_tokens=1000
                  )

                  return {
                      "niche": niche,
                      "analysis": response.choices[0].message.content,
                      "status": "completed"
                  }
              except Exception as e:
                  logger.error(f"Niche analysis failed: {str(e)}")
                  return {"niche": niche, "status": "failed", "error": str(e)}

          def _generate_art(self, niche: str, num_images: int) -> Dict[str, Any]:
              """
              Generate art variations for the niche.
              Delegates to ArtGenerationAgent with DALL-E 3 in production.
              """
              logger.info(f"Generating {num_images} art variations for {niche}")
              # In production, this will call ArtGenerationAgent which uses DALL-E 3
              # For now, return placeholder structure
              return {
                  "niche": niche,
                  "num_images": num_images,
                  "images": [
                      {
                          "id": f"img_{i}",
                          "prompt": f"{niche} design variation {i+1}",
                          "url": f"https://placeholder.com/{i}",
                          "style": ["minimalist", "watercolor", "abstract"][i % 3]
                      }
                      for i in range(min(num_images, 5))  # Return 5 for demo
                  ],
                  "status": "generated"
              }

          def _create_listings(self, niche: str, num_listings: int, art_gen: Dict) -> Dict[str, Any]:
              """
              Create SEO-optimized Etsy listings.
              Delegates to ListingManagerAgent in production.
              """
              logger.info(f"Creating {num_listings} Etsy listings")
              # In production, this will call ListingManagerAgent with Etsy API
              return {
                  "niche": niche,
                  "num_listings": num_listings,
                  "listings": [
                      {
                          "id": f"listing_{i}",
                          "title": f"{niche} Art Print - Design {i+1}",
                          "description": f"Beautiful {niche} artwork perfect for home decoration",
                          "price": 15.99 + (i * 0.50),
                          "tags": ["art", "print", niche.split()[0].lower()]
                      }
                      for i in range(num_listings)
                  ],
                  "status": "created"
              }

          def _schedule_tiktok_content(self, niche: str, num_posts: int) -> Dict[str, Any]:
              """
              Schedule TikTok content distribution.
              Delegates to TikTokManagerAgent in production.
              """
              logger.info(f"Scheduling {num_posts} TikTok posts")
              # In production, this will call TikTokManagerAgent
              return {
                  "niche": niche,
                  "num_posts": num_posts,
                  "posts": [
                      {
                          "id": f"tiktok_{i}",
                          "caption": f"Check out our new {niche} design! #art #design #{niche.lower().replace(' ', '')}",
                          "scheduled_time": f"2026-01-{(i % 30) + 1:02d} {(i % 24):02d}:00"
                      }
                      for i in range(num_posts)
                  ],
                  "status": "scheduled"
              }

          def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
              """Get status of a specific workflow."""
              for execution in self.execution_history:
                  if execution.get("workflow_id") == workflow_id:
                      return execution
              return {"error": f"Workflow {workflow_id} not found"}

          def get_execution_history(self) -> list:
              """Get all workflow executions."""
              return self.execution_history

          def get_current_state(self) -> Dict[str, Any]:
              """Get current workflow state."""
              return self.workflow_state
      
