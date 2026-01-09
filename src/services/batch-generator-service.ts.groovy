// Batch Image Generator Service
// Generates 25-100 themed images from Leonardo.AI API

import { prisma } from './prisma';
import { env } from './env';
import axios from 'axios';

// Type definitions
export interface BatchConfig {
      theme: string;
        count: number;  // 25-100 images
          userId: string;
}

export interface BatchResult {
      batchId: string;
        theme: string;
          imagesGenerated: number;
            totalCount: number;
              startedAt: Date;
                completedAt: Date;
                  status: 'success' | 'failed';
                    error?: string;
}

// Theme templates with variations
const THEME_TEMPLATES = {
      'nursery-animals': {
            subjects: ['bunny', 'deer', 'lamb', 'duckling', 'kitten', 'puppy', 'fox kit'],
                styles: ['watercolor', 'illustration', 'soft painting', 'cute cartoon'],
                    settings: ['forest', 'meadow', 'clouds', 'nature background'],
                        colors: ['sage green', 'soft pink', 'cream', 'pastel blue']
      },
        'gothic-landscapes': {
                subjects: ['castle', 'forest', 'mountains', 'lake', 'cliff', 'graveyard'],
                    styles: ['dark painting', 'gothic art', 'oil painting', 'moody'],
                        settings: ['moonlight', 'storm', 'mist', 'twilight'],
                            colors: ['deep purple', 'charcoal', 'blood red', 'silver']
        },
          'abstract-modern': {
                subjects: ['geometric shapes', 'abstract patterns', 'flowing forms', 'color blocks'],
                    styles: ['minimalist', 'modern art', 'geometric', 'contemporary'],
                        settings: ['clean background', 'gradient', 'solid color', 'pattern'],
                            colors: ['black', 'white', 'navy', 'gold', 'blush pink']
          },
            'botanical': {
                    subjects: ['flower', 'leaf', 'plant', 'branch', 'herb', 'fern', 'succulent'],
                        styles: ['botanical illustration', 'scientific drawing', 'watercolor', 'engraving'],
                            settings: ['white background', 'aged paper', 'natural light'],
                                colors: ['green', 'brown', 'cream', 'gold']
            },
              'vintage-french': {
                    subjects: ['rose', 'peony', 'lavender', 'lily', 'floral arrangement', 'wreath'],
                        styles: ['vintage poster', 'french art', 'decorative', 'romantic illustration'],
                            settings: ['ornate frame', 'aged background', 'damask pattern'],
                                colors: ['rose pink', 'cream', 'gold', 'sage green']
              }
};

// Helper function to generate prompt variations
function generatePrompt(theme: string, index: number): string {
      const templates = THEME_TEMPLATES[theme as keyof typeof THEME_TEMPLATES] || THEME_TEMPLATES['abstract-modern'];
        
          const subject = templates.subjects[index % templates.subjects.length];
            const style = templates.styles[Math.floor(index / templates.subjects.length) % templates.styles.length];
              const setting = templates.settings[Math.floor((index * 2) / templates.subjects.length) % templates.settings.length];
                const color = templates.colors[Math.floor((index * 3) / templates.subjects.length) % templates.colors.length];
                  
                    return `${subject}, ${style}, ${setting}, ${color} colors, professional quality, high resolution`;
}

// Main batch generation function
export async function generateBatch(config: BatchConfig): Promise<BatchResult> {
      const startTime = new Date();
        let generatedCount = 0;
          const batchId = `batch_${Date.now()}_${Math.random().toString(36).substring(7)}`;
            
              try {
                    // Validate inputs
                        if (config.count < 25 || config.count > 100) {
                                  throw new Error('Image count must be between 25 and 100');
                        }
                            
                                if (!THEME_TEMPLATES[config.theme as keyof typeof THEME_TEMPLATES]) {
                                          throw new Error(`Theme "${config.theme}" not found. Available: ${Object.keys(THEME_TEMPLATES).join(', ')}`);
                                }
                                    
                                        // Create Bundle record in database
                                            const bundle = await prisma.bundle.create({
                                                      data: {
                                                                batchId,
                                                                        themeName: config.theme,
                                                                                imageCount: config.count,
                                                                                        status: 'generating',
                                                                                                userId: config.userId
                                                      }
                                            });
                                                
                                                    console.log(`Starting batch generation: ${batchId}, Theme: ${config.theme}, Count: ${config.count}`);
                                                        
                                                            // Generate images
                                                                for (let i = 0; i < config.count; i++) {
                                                                          try {
                                                                                    const prompt = generatePrompt(config.theme, i);
                                                                                            
                                                                                                    console.log(`Generating image ${i + 1}/${config.count}...`);
                                                                                                            
                                                                                                                    // Call Leonardo.AI API
                                                                                                                            const response = await axios.post(
                                                                                                                                          'https://api.leonardo.ai/rest/v1/generations',
                                                                                                                                                    {
                                                                                                                                                                    prompt: prompt,
                                                                                                                                                                                width: 1024,
                                                                                                                                                                                            height: 1024,
                                                                                                                                                                                                        num_images: 1,
                                                                                                                                                                                                                    quality: 'standard'
                                                                                                                                                    },
                                                                                                                                                              {
                                                                                                                                                                            headers: {
                                                                                                                                                                                              'Authorization': `Bearer ${env.LEONARDO_API_KEY}`,
                                                                                                                                                                                                            'Content-Type': 'application/json'
                                                                                                                                                                            }
                                                                                                                                                              }
                                                                                                                            );
                                                                                                                                    
                                                                                                                                            // Check if generation was successful
                                                                                                                                                    if (response.data && response.data.sdGenerationJob && response.data.sdGenerationJob.generationId) {
                                                                                                                                                                  const generationId = response.data.sdGenerationJob.generationId;
                                                                                                                                                                            
                                                                                                                                                                                      // Poll for image URL
                                                                                                                                                                                                let imageUrl = null;
                                                                                                                                                                                                          let pollAttempts = 0;
                                                                                                                                                                                                                    while (!imageUrl && pollAttempts < 30) {
                                                                                                                                                                                                                                    await new Promise(r => setTimeout(r, 500)); // Wait 500ms between polls
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                            const statusResponse = await axios.get(
                                                                                                                                                                                                                                                                              `https://api.leonardo.ai/rest/v1/generations/${generationId}`,
                                                                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                                                                                headers: {
                                                                                                                                                                                                                                                                                                                                      'Authorization': `Bearer ${env.LEONARDO_API_KEY}`
                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                            );
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                    if (statusResponse.data && statusResponse.data.generations_by_pk && statusResponse.data.generations_by_pk.generated_images && statusResponse.data.generations_by_pk.generated_images.length > 0) {
                                                                                                                                                                                                                                                                                                      imageUrl = statusResponse.data.generations_by_pk.generated_images[0].url;
                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                            pollAttempts++;
                                                                                                                                                                                                                    }
                                                                                                                                                                                                                              
                                                                                                                                                                                                                                        if (imageUrl) {
                                                                                                                                                                                                                                                        // Save image metadata to database
                                                                                                                                                                                                                                                                    await prisma.batchedImage.create({
                                                                                                                                                                                                                                                                                      data: {
                                                                                                                                                                                                                                                                                                        batchId,
                                                                                                                                                                                                                                                                                                                        url: imageUrl,
                                                                                                                                                                                                                                                                                                                                        prompt: prompt,
                                                                                                                                                                                                                                                                                                                                                        theme: config.theme,
                                                                                                                                                                                                                                                                                                                                                                        order: i + 1,
                                                                                                                                                                                                                                                                                                                                                                                        width: 1024,
                                                                                                                                                                                                                                                                                                                                                                                                        height: 1024
                                                                                                                                                                                                                                                                                      }
                                                                                                                                                                                                                                                                    });
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                            generatedCount++;
                                                                                                                                                                                                                                                                                                        console.log(`✓ Image ${i + 1}/${config.count} generated successfully`);
                                                                                                                                                                                                                                        } else {
                                                                                                                                                                                                                                                        console.log(`✗ Image ${i + 1}/${config.count} failed - timeout waiting for image URL`);
                                                                                                                                                                                                                                        }
                                                                                                                                                    } else {
                                                                                                                                                                  console.log(`✗ Image ${i + 1}/${config.count} failed - invalid API response`);
                                                                                                                                                    }
                                                                                                                                                            
                                                                                                                                                                    // Rate limiting: wait 500ms between API calls
                                                                                                                                                                            await new Promise(r => setTimeout(r, 500));
                                                                                                                                                                                    
                                                                          } catch (error: any) {
                                                                                    console.error(`Error generating image ${i + 1}/${config.count}:`, error.message);
                                                                                            // Continue with next image instead of failing entire batch
                                                                          }
                                                                }
                                                                    
                                                                        // Update bundle status
                                                                            await prisma.bundle.update({
                                                                                      where: { id: bundle.id },
                                                                                            data: {
                                                                                                        status: 'generated',
                                                                                                                imageCount: generatedCount
                                                                                            }
                                                                            });
                                                                                
                                                                                    const endTime = new Date();
                                                                                        console.log(`✓ Batch generation complete: ${generatedCount}/${config.count} images generated`);
                                                                                            
                                                                                                return {
                                                                                                          batchId,
                                                                                                                theme: config.theme,
                                                                                                                      imagesGenerated: generatedCount,
                                                                                                                            totalCount: config.count,
                                                                                                                                  startedAt: startTime,
                                                                                                                                        completedAt: endTime,
                                                                                                                                              status: generatedCount > 0 ? 'success' : 'failed',
                                                                                                                                                    error: generatedCount === 0 ? 'No images were generated' : undefined
                                                                                                };
                                                                                                    
              } catch (error: any) {
                    console.error(`Batch generation failed: ${error.message}`);
                        
                            // Update bundle status to failed
                                try {
                                          await prisma.bundle.updateMany({
                                                    where: { batchId },
                                                            data: { status: 'failed' }
                                          });
                                } catch (updateError) {
                                          console.error('Failed to update bundle status:', updateError);
                                }
                                    
                                        return {
                                                  batchId,
                                                        theme: config.theme,
                                                              imagesGenerated: generatedCount,
                                                                    totalCount: config.count,
                                                                          startedAt: startTime,
                                                                                completedAt: new Date(),
                                                                                      status: 'failed',
                                                                                            error: error.message
                                        };
              }
}

// Helper function to get batch status
export async function getBatchStatus(batchId: string) {
      const batch = await prisma.bundle.findUnique({
            where: { batchId },
                include: {
                          // If we add relation to BatchedImage in schema
                }
      });
        
          const images = await prisma.batchedImage.findMany({
                where: { batchId }
          });
            
              return {
                    batchId,
                        status: batch?.status || 'not_found',
                            imagesGenerated: images.length,
                                totalImages: batch?.imageCount || 0,
                                    theme: batch?.themeName || null,
                                        createdAt: batch?.createdAt
              };
}


              }
          })
                }
      })
}
                                        }
                                }
                                          })
                                }
              }
                                                                                                }
                                                                                            }
                                                                            })
                                                                          }
                                                                                                                                                    }
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                      }
                                                                                                                                                                                                                                                                    })
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                            )
                                                                                                                                                                                                                    }
                                                                                                                                                    }
                                                                                                                                                                            }
                                                                                                                                                              }
                                                                                                                                                    }
                                                                                                                            )
                                                                          }
                                                                }
                                                      }
                                            })
                                }
                        }
              }
}
}
              }
            }
          }
        }
      }
}
}
}