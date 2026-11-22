import os
import docx
from docx_helpers import setup_document
from pages_1_to_4 import build_page_1, build_page_2, build_page_3, build_page_4
from pages_5_to_8 import build_page_5, build_page_6, build_page_7, build_page_8
from pages_9_to_12 import build_page_9, build_page_10, build_page_11, build_page_12

def main():
    print("Initializing document setup with micro-print parameters...")
    doc = setup_document()
    
    pages = [
        ("Page 1: AI Foundations, Evolution, PEAS & Environments", build_page_1),
        ("Page 2: Structure of Intelligent Agents (5 Architectures)", build_page_2),
        ("Page 3: Problem Solving & Search (UCS, Heuristics, Hill Climbing)", build_page_3),
        ("Page 4: Informed Search (A* Search, Observations, CSP)", build_page_4),
        ("Page 5: Adversarial Search (Minimax & Alpha-Beta Pruning)", build_page_5),
        ("Page 6: Knowledge Representation (Issues, Approaches, Propositional Logic)", build_page_6),
        ("Page 7: First-Order Predicate Logic & Forward/Backward Chaining", build_page_7),
        ("Page 8: Probabilistic Reasoning (Bayesian Networks, Dempster-Shafer)", build_page_8),
        ("Page 9: Fuzzy Sets & AI Planning (STRIPS Block World)", build_page_9),
        ("Page 10: Natural Language Processing (Syntactic vs Semantic)", build_page_10),
        ("Page 11: Expert Systems (Architecture, Roles, Shells, Applications)", build_page_11),
        ("Page 12: Comprehensive Solved Objective & MCQ Bank", build_page_12)
    ]
    
    for i, (name, builder) in enumerate(pages):
        print(f"Building {name}...")
        builder(doc)
        if i < len(pages) - 1:
            doc.add_page_break()
            
    output_docx = "open-book-notes.docx"
    doc.save(output_docx)
    print(f"Successfully generated and saved {output_docx} ({os.path.getsize(output_docx)} bytes)")

if __name__ == "__main__":
    main()
