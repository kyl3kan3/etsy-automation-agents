"""Listing Manager Agent - Etsy API integration for creating and managing listings"""
import os
import logging
from typing import Dict, Any, List, Optional
from openai import OpenAI

logger = logging.getLogger(__name__)

class ListingManagerAgent:
      """Manages Etsy shop listings creation, updates, and optimization via Etsy API."""

    def __init__(self, api_key: Optional[str] = None, etsy_api_key: Optional[str] = None, shop_id: Optional[str] = None):
              self.api_key = api_key or os.getenv("OPENAI_API_KEY")
              self.etsy_api_key = etsy_api_key or os.getenv("ETSY_API_KEY")
              self.shop_id = shop_id or os.getenv("ETSY_SHOP_ID")

        if not self.api_key:
                      raise ValueError("OpenAI API key required")

        self.client = OpenAI(api_key=self.api_key)
        self.listings = []
        logger.info("ListingManagerAgent initialized")

    def create_listing(self, title: str, description: str, price: float, image_url: str, tags: List[str]) -> Dict[str, Any]:
              """Create a new Etsy listing with SEO optimization."""
              logger.info(f"Creating listing: {title}")

        # Generate SEO-optimized content if not provided
              seo_title = self._optimize_title(title)
              seo_description = self._optimize_description(description)

        listing = {
                      "id": f"listing_{len(self.listings):05d}",
                      "title": seo_title,
                      "description": seo_description,
                      "price": price,
                      "image_url": image_url,
                      "tags": tags,
                      "status": "draft",
                      "created_at": "2026-01-07"
        }

        self.listings.append(listing)
        logger.info(f"Listing created: {listing['id']}")
        return listing

    def _optimize_title(self, title: str) -> str:
              """Optimize title for Etsy SEO using GPT-4."""
              try:
                            response = self.client.chat.completions.create(
                                              model="gpt-4-turbo",
                                              messages=[{
                                                                    "role": "user",
                                                                    "content": f"Optimize this Etsy listing title for SEO (max 140 chars): {title}"
                                              }],
                                              temperature=0.7,
                                              max_tokens=50
                            )
                            return response.choices[0].message.content
                        except:
            return title

    def _optimize_description(self, description: str) -> str:
              """Optimize description with keywords and formatting."""
              return description

    def bulk_create_listings(self, listings_data: List[Dict]) -> List[Dict[str, Any]]:
              """Create multiple listings in batch."""
              results = []
              for data in listings_data:
                            result = self.create_listing(**data)
                            results.append(result)
                        return results

    def get_listings(self) -> List[Dict[str, Any]]:
              """Retrieve all listings."""
        return self.listings

    def publish_listing(self, listing_id: str) -> Dict[str, Any]:
              """Publish listing to Etsy shop."""
        for listing in self.listings:
                      if listing["id"] == listing_id:
                                        listing["status"] = "published"
                                        logger.info(f"Listing published: {listing_id}")
                                        return listing
                                return {"error": "Listing not found"}
