#!/usr/bin/env python3
"""
Research Graph CLI - Node Details Viewer
A command-line interface for exploring research paper details.
This prototype demonstrates why CLI is not suitable for this use case.
"""

import json
import sys
from typing import Dict, List, Any

class ResearchGraphCLI:
    def __init__(self):
        self.paper_data = {
            "title": "Graph Neural Networks for Recommendation Systems",
            "authors": ["Zhang", "Li", "Wang"],
            "year": 2023,
            "venue": "ICML",
            "citations": 127,
            "abstract": "This paper presents a novel approach to recommendation systems using graph neural networks. We introduce a multi-layer GNN architecture that captures both local and global user-item interactions, achieving state-of-the-art performance on multiple datasets.",
            "contributions": [
                "Novel GNN architecture for recommendation systems",
                "Solution to cold-start problem",
                "State-of-the-art performance on benchmark datasets",
                "Open-source implementation available"
            ],
            "related_papers": [
                {
                    "type": "Cited By",
                    "title": "Deep Learning for Collaborative Filtering",
                    "description": "Extends our work with attention mechanisms"
                },
                {
                    "type": "References",
                    "title": "Graph Convolutional Networks", 
                    "description": "Foundational work on GCNs"
                }
            ],
            "metrics": {
                "impact_score": 4.2,
                "reproducibility": 87,
                "implementation_ready": "High"
            }
        }

    def display_header(self):
        """Display ASCII art header"""
        print("=" * 80)
        print("  RESEARCH GRAPH CLI - NODE DETAILS VIEWER")
        print("=" * 80)
        print()

    def display_paper_info(self):
        """Display basic paper information"""
        print(f"TITLE: {self.paper_data['title']}")
        print(f"AUTHORS: {', '.join(self.paper_data['authors'])}")
        print(f"YEAR: {self.paper_data['year']}")
        print(f"VENUE: {self.paper_data['venue']}")
        print(f"CITATIONS: {self.paper_data['citations']}")
        print("-" * 80)

    def display_abstract(self):
        """Display paper abstract"""
        print("ABSTRACT:")
        print("-" * 20)
        # Wrap text at 70 characters
        words = self.paper_data['abstract'].split()
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line + word) > 70:
                lines.append(current_line.strip())
                current_line = word + " "
            else:
                current_line += word + " "
        
        if current_line:
            lines.append(current_line.strip())
            
        for line in lines:
            print(line)
        print()

    def display_contributions(self):
        """Display key contributions"""
        print("KEY CONTRIBUTIONS:")
        print("-" * 20)
        for i, contribution in enumerate(self.paper_data['contributions'], 1):
            print(f"{i}. {contribution}")
        print()

    def display_related_papers(self):
        """Display related papers"""
        print("RELATED PAPERS:")
        print("-" * 20)
        for paper in self.paper_data['related_papers']:
            print(f"[{paper['type']}] {paper['title']}")
            print(f"  {paper['description']}")
            print()
        print()

    def display_metrics(self):
        """Display paper metrics"""
        print("METRICS:")
        print("-" * 20)
        metrics = self.paper_data['metrics']
        print(f"Impact Score: {metrics['impact_score']}")
        print(f"Reproducibility: {metrics['reproducibility']}%")
        print(f"Implementation Ready: {metrics['implementation_ready']}")
        print()

    def display_menu(self):
        """Display interactive menu"""
        print("COMMANDS:")
        print("-" * 20)
        print("1. Show abstract")
        print("2. Show contributions") 
        print("3. Show related papers")
        print("4. Show metrics")
        print("5. Export to JSON")
        print("6. Exit")
        print()

    def export_json(self):
        """Export paper data to JSON"""
        filename = "paper_details.json"
        with open(filename, 'w') as f:
            json.dump(self.paper_data, f, indent=2)
        print(f"Data exported to {filename}")

    def run_interactive(self):
        """Run interactive CLI session"""
        self.display_header()
        self.display_paper_info()
        
        while True:
            self.display_menu()
            try:
                choice = input("Enter command (1-6): ").strip()
                
                if choice == "1":
                    self.display_abstract()
                elif choice == "2":
                    self.display_contributions()
                elif choice == "3":
                    self.display_related_papers()
                elif choice == "4":
                    self.display_metrics()
                elif choice == "5":
                    self.export_json()
                elif choice == "6":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter 1-6.")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

    def run_non_interactive(self):
        """Run non-interactive mode showing all information"""
        self.display_header()
        self.display_paper_info()
        self.display_abstract()
        self.display_contributions()
        self.display_related_papers()
        self.display_metrics()

def main():
    cli = ResearchGraphCLI()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        cli.run_non_interactive()
    else:
        cli.run_interactive()

if __name__ == "__main__":
    main()
