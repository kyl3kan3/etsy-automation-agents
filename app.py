"""Flask backend API for Etsy Automation System with Vue.js frontend"""
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
import logging
from datetime import datetime

# Import agents
from agents.orchestrator import OrchestratorAgent
from agents.niche_discovery import NicheDiscoveryAgent
from agents.art_generation import ArtGenerationAgent
from agents.listing_manager import ListingManagerAgent
from agents.tiktok_manager import TikTokManagerAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Initialize agents
orchestrator = OrchestratorAgent()
niche_agent = NicheDiscoveryAgent()
art_agent = ArtGenerationAgent()
listing_agent = ListingManagerAgent()
tiktok_agent = TikTokManagerAgent()

@app.route('/')
def index():
    """Serve the main dashboard HTML"""
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    """Get system status"""
    return jsonify({
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "agents": {
            "orchestrator": "ready",
            "niche_discovery": "ready",
            "art_generation": "ready",
            "listing_manager": "ready",
            "tiktok_manager": "ready"
        }
    })

@app.route('/api/workflow', methods=['POST'])
def start_workflow():
    """Start automation workflow for a niche"""
    try:
        data = request.json
        niche = data.get('niche')
        num_images = data.get('num_images', 50)
        num_listings = data.get('num_listings', 10)

        if not niche:
            return jsonify({"error": "Niche is required"}), 400

        logger.info(f"Starting workflow for niche: {niche}")
        result = orchestrator.run_workflow(niche, num_images, num_listings)

        return jsonify(result)
    except Exception as e:
        logger.error(f"Workflow failed: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/niche/analyze', methods=['POST'])
def analyze_niche():
    """Analyze a niche"""
    try:
        data = request.json
        niche = data.get('niche')

        if not niche:
            return jsonify({"error": "Niche is required"}), 400

        logger.info(f"Analyzing niche: {niche}")
        result = niche_agent.analyze_niche(niche)

        return jsonify(result)
    except Exception as e:
        logger.error(f"Niche analysis failed: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/trending-niches')
def get_trending_niches():
    """Get trending niches"""
    try:
        trending = niche_agent.get_trending_niches(limit=10)
        return jsonify({"niches": trending})
    except Exception as e:
        logger.error(f"Failed to get trending niches: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/images/generate', methods=['POST'])
def generate_images():
    """Generate art images"""
    try:
        data = request.json
        niche = data.get('niche')
        num_images = data.get('num_images', 50)

        if not niche:
            return jsonify({"error": "Niche is required"}), 400

        logger.info(f"Generating {num_images} images for {niche}")
        result = art_agent.generate_images(niche, num_images)

        return jsonify(result)
    except Exception as e:
        logger.error(f"Image generation failed: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/listings', methods=['GET', 'POST'])
def manage_listings():
    """Get or create listings"""
    try:
        if request.method == 'GET':
            listings = listing_agent.get_listings()
            return jsonify({"listings": listings})
        else:
            data = request.json
            result = listing_agent.create_listing(**data)
            return jsonify(result)
    except Exception as e:
        logger.error(f"Listing management failed: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/listings/<listing_id>/publish', methods=['POST'])
def publish_listing(listing_id):
    """Publish a listing"""
    try:
        result = listing_agent.publish_listing(listing_id)
        return jsonify(result)
    except Exception as e:
        logger.error(f"Listing publish failed: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/tiktok/posts', methods=['GET', 'POST'])
def manage_tiktok_posts():
    """Get or create TikTok posts"""
    try:
        if request.method == 'GET':
            posts = tiktok_agent.get_scheduled_posts()
            return jsonify({"posts": posts})
        else:
            data = request.json
            result = tiktok_agent.schedule_post(**data)
            return jsonify(result)
    except Exception as e:
        logger.error(f"TikTok post management failed: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/tiktok/captions', methods=['POST'])
def generate_captions():
    """Generate TikTok captions"""
    try:
        data = request.json
        niche = data.get('niche')
        num_captions = data.get('num_captions', 10)

        if not niche:
            return jsonify({"error": "Niche is required"}), 400

        captions = tiktok_agent.generate_captions(niche, num_captions)
        return jsonify({"captions": captions})
    except Exception as e:
        logger.error(f"Caption generation failed: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/workflow/history')
def get_workflow_history():
    """Get workflow execution history"""
    try:
        history = orchestrator.get_execution_history()
        return jsonify({"history": history})
    except Exception as e:
        logger.error(f"Failed to get history: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




# Import batch generator
from agents.batch_generator import BatchGeneratorAgent

# Initialize batch generator agent
batch_agent = BatchGeneratorAgent()

# ==================== BATCH GENERATION ROUTES ====================

@app.route('/api/bundles/generate', methods=['POST'])
def generate_bundle():
    """Generate a batch of themed images"""
        try:
                data = request.get_json()
                        theme = data.get('theme')
                                count = data.get('count', 50)
                                        
                                                if not theme:
                                                            return jsonify({'error': 'Theme is required'}), 400
                                                                    
                                                                            # Generate batch
                                                                                    result = batch_agent.generate_batch(theme, count)
                                                                                            
                                                                                                    return jsonify(result), 200 if result['status'] == 'success' else 400
                                                                                                            
                                                                                                                except Exception as e:
                                                                                                                        logger.error(f"Error generating bundle: {str(e)}")
                                                                                                                                return jsonify({'error': str(e)}), 500

                                                                                                                                @app.route('/api/bundles/<batch_id>/status', methods=['GET'])
                                                                                                                                def get_bundle_status(batch_id):
                                                                                                                                    """Get status of a batch generation"""
                                                                                                                                        try:
                                                                                                                                                result = batch_agent.get_batch_status(batch_id)
                                                                                                                                                        return jsonify(result), 200
                                                                                                                                                            except Exception as e:
                                                                                                                                                                    logger.error(f"Error getting bundle status: {str(e)}")
                                                                                                                                                                            return jsonify({'error': str(e)}), 500

                                                                                                                                                                            @app.route('/api/bundles/themes', methods=['GET'])
                                                                                                                                                                            def get_available_themes():
                                                                                                                                                                                """Get list of available bundle themes"""
                                                                                                                                                                                    return jsonify({
                                                                                                                                                                                            'themes': list(batch_agent.theme_templates.keys()),
                                                                                                                                                                                                    'description': 'Available themes for bundle generation'
                                                                                                                                                                                                        }), 200
                                                                                                                                                                                                        