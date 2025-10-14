#!/usr/bin/env python3
"""
Personal Research Library CLI - Command Line Interface
A command-line interface for managing personal research papers and folders.
This prototype demonstrates why CLI is not suitable for personal library management.
"""

import json
import os
import sys
from typing import Dict, List, Any
from datetime import datetime

class PersonalLibraryCLI:
    def __init__(self):
        self.library_file = "personal_library.json"
        self.library_data = self.load_library()
        
    def load_library(self) -> Dict[str, Any]:
        """Load library data from JSON file"""
        if os.path.exists(self.library_file):
            with open(self.library_file, 'r') as f:
                return json.load(f)
        else:
            return {
                "user": "Madison Davis",
                "folders": [
                    {
                        "name": "Graph Neural Networks",
                        "papers": [
                            {
                                "title": "Graph Neural Networks for Recommendation Systems",
                                "authors": "Zhang et al.",
                                "year": 2023,
                                "citations": 127,
                                "summary": "Novel GNN architecture for recommendation systems"
                            }
                        ]
                    }
                ],
                "starred_papers": [],
                "recommendations": []
            }
    
    def save_library(self):
        """Save library data to JSON file"""
        with open(self.library_file, 'w') as f:
            json.dump(self.library_data, f, indent=2)
    
    def display_header(self):
        """Display ASCII art header"""
        print("=" * 80)
        print("  PERSONAL RESEARCH LIBRARY CLI")
        print("=" * 80)
        print(f"User: {self.library_data['user']}")
        print(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("=" * 80)
        print()
    
    def display_stats(self):
        """Display library statistics"""
        total_papers = sum(len(folder['papers']) for folder in self.library_data['folders'])
        total_folders = len(self.library_data['folders'])
        starred_count = len(self.library_data['starred_papers'])
        
        print("LIBRARY STATISTICS:")
        print("-" * 20)
        print(f"Total Papers: {total_papers}")
        print(f"Folders: {total_folders}")
        print(f"Starred Papers: {starred_count}")
        print(f"Recommendations: {len(self.library_data['recommendations'])}")
        print()
    
    def display_folders(self):
        """Display all folders"""
        print("FOLDERS:")
        print("-" * 20)
        for i, folder in enumerate(self.library_data['folders'], 1):
            print(f"{i}. {folder['name']} ({len(folder['papers'])} papers)")
            if folder['papers']:
                print("   Recent papers:")
                for paper in folder['papers'][:2]:  # Show only first 2
                    print(f"   - {paper['title'][:60]}...")
            print()
    
    def display_papers_in_folder(self, folder_index: int):
        """Display papers in a specific folder"""
        if 0 <= folder_index < len(self.library_data['folders']):
            folder = self.library_data['folders'][folder_index]
            print(f"PAPERS IN: {folder['name']}")
            print("-" * 40)
            
            for i, paper in enumerate(folder['papers'], 1):
                print(f"{i}. {paper['title']}")
                print(f"   Authors: {paper['authors']}")
                print(f"   Year: {paper['year']}, Citations: {paper['citations']}")
                print(f"   Summary: {paper['summary']}")
                print()
        else:
            print("Invalid folder index!")
    
    def display_starred_papers(self):
        """Display starred papers"""
        print("STARRED PAPERS:")
        print("-" * 20)
        if self.library_data['starred_papers']:
            for i, paper in enumerate(self.library_data['starred_papers'], 1):
                print(f"{i}. {paper['title']}")
                print(f"   {paper['authors']} ({paper['year']})")
                print()
        else:
            print("No starred papers yet.")
        print()
    
    def display_recommendations(self):
        """Display AI recommendations"""
        print("AI RECOMMENDATIONS:")
        print("-" * 20)
        if self.library_data['recommendations']:
            for i, rec in enumerate(self.library_data['recommendations'], 1):
                print(f"{i}. {rec['title']}")
                print(f"   Reason: {rec['reason']}")
                print(f"   Confidence: {rec['confidence']}%")
                print()
        else:
            print("No recommendations available.")
        print()
    
    def add_paper_to_folder(self, folder_index: int):
        """Add a new paper to a folder"""
        if 0 <= folder_index < len(self.library_data['folders']):
            print("ADD NEW PAPER:")
            print("-" * 20)
            title = input("Paper title: ")
            authors = input("Authors: ")
            year = input("Year: ")
            citations = input("Citations: ")
            summary = input("Summary: ")
            
            new_paper = {
                "title": title,
                "authors": authors,
                "year": int(year),
                "citations": int(citations),
                "summary": summary
            }
            
            self.library_data['folders'][folder_index]['papers'].append(new_paper)
            self.save_library()
            print("Paper added successfully!")
        else:
            print("Invalid folder index!")
    
    def create_folder(self):
        """Create a new folder"""
        print("CREATE NEW FOLDER:")
        print("-" * 20)
        name = input("Folder name: ")
        description = input("Description: ")
        
        new_folder = {
            "name": name,
            "description": description,
            "papers": []
        }
        
        self.library_data['folders'].append(new_folder)
        self.save_library()
        print(f"Folder '{name}' created successfully!")
    
    def display_menu(self):
        """Display interactive menu"""
        print("COMMANDS:")
        print("-" * 20)
        print("1. Show library statistics")
        print("2. List all folders")
        print("3. View papers in folder")
        print("4. Show starred papers")
        print("5. Show AI recommendations")
        print("6. Add paper to folder")
        print("7. Create new folder")
        print("8. Export library to JSON")
        print("9. Exit")
        print()
    
    def export_library(self):
        """Export library to JSON"""
        export_file = f"library_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(export_file, 'w') as f:
            json.dump(self.library_data, f, indent=2)
        print(f"Library exported to {export_file}")
    
    def run_interactive(self):
        """Run interactive CLI session"""
        self.display_header()
        self.display_stats()
        
        while True:
            self.display_menu()
            try:
                choice = input("Enter command (1-9): ").strip()
                
                if choice == "1":
                    self.display_stats()
                elif choice == "2":
                    self.display_folders()
                elif choice == "3":
                    folder_idx = int(input("Enter folder number: ")) - 1
                    self.display_papers_in_folder(folder_idx)
                elif choice == "4":
                    self.display_starred_papers()
                elif choice == "5":
                    self.display_recommendations()
                elif choice == "6":
                    folder_idx = int(input("Enter folder number: ")) - 1
                    self.add_paper_to_folder(folder_idx)
                elif choice == "7":
                    self.create_folder()
                elif choice == "8":
                    self.export_library()
                elif choice == "9":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter 1-9.")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def run_demo(self):
        """Run demo mode showing all information"""
        self.display_header()
        self.display_stats()
        self.display_folders()
        self.display_starred_papers()
        self.display_recommendations()
        
        print("ISSUES WITH CLI APPROACH:")
        print("-" * 30)
        print("1. Poor readability for paper summaries and descriptions")
        print("2. No visual hierarchy or formatting")
        print("3. Difficult to browse and compare papers")
        print("4. No way to display visual relationships between papers")
        print("5. Poor user experience for researchers who need quick scanning")
        print("6. No support for rich media (images, charts, etc.)")
        print("7. Limited interactivity and exploration capabilities")
        print("8. No visual folder structure or organization")
        print("9. Difficult to manage large collections of papers")
        print("10. No way to visualize paper relationships or citations")

def main():
    cli = PersonalLibraryCLI()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        cli.run_demo()
    else:
        cli.run_interactive()

if __name__ == "__main__":
    main()
