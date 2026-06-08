"""
Quiz data for the Hazardous Property Codes quiz.

Contains two dictionaries:
- quiz_questions: 14 Hazard Property (HP) codes and their shortened definitions for uses as the main quiz content.
- tutorial_questions: 2 HP codes used in the tutorial screen to demonstrate how the matching quiz works before the player begins.
"""

quiz_questions = { "HP_1 Explosive" : "Causes dangerous chemical reactions that can damage surroundings",
                  "HP_2 Oxidizing" : "Provides oxygen, causing or contributing to the combustion of other materials",
                  "HP_3 Flammable" : "Easily ignites, inc. liquids with flashpoint below 60°C, flammable gases, or solid waste",
                  "HP_4 Irritant" :	"Causes skin irritation or damage to the eyes upon contact",
                  "HP_5 Organ/Aspiration Toxicity" : "Harms specific organs or cause toxic effects when inhaled or absorbed",
                  "HP_6 Acute Toxicity" : "Causes severe health effects when ingested, inhaled, or through skin contact",
                  "HP_7 Carcinogenic" : "Can cause cancer or increase the risk of cancer",
                  "HP_8 Corrosive" : "Causes severe skin corrosion upon contact",
                  "HP_9 Infectious" : "Contains microorganisms or toxins that can cause disease in humans or animals",
                  "HP_10 Toxic for Reproduction" : "May negatively affect reproductive health or harm offspring development",
                  "HP_11 Mutagenic" : "Causes permanent changes in genetic material",
                  "HP_12 Produces Toxic Gases" : "Releases toxic gases when in contact with water or acids",
                  "HP_13 Sensitising" : "Causes allergic reactions, affecting the skin or respiratory system",
                  "HP_14 Ecotoxic" : "Poses risks to the environment, potentially affecting ecosystems"}

tutorial_questions = {"HP_15" : "May show any of the hazardous properties, even if not initially present",
                      "HP_POP" : "Contains persistent organic pollutants above the concentration limit"}
                  