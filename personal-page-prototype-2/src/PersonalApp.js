import React, { useState } from 'react';
import './PersonalApp.css';

function PersonalApp() {
  const [selectedFolder, setSelectedFolder] = useState(null);
  const [viewMode, setViewMode] = useState('folders'); // 'folders', 'papers', 'recommendations'

  const folders = [
    {
      id: 1,
      name: "Graph Neural Networks",
      icon: "📊",
      count: 12,
      description: "Research on GNN architectures",
      papers: [
        {
          title: "Graph Neural Networks for Recommendation Systems",
          authors: "Zhang et al.",
          year: 2023,
          citations: 127,
          summary: "Novel GNN architecture for recommendation systems"
        },
        {
          title: "Graph Convolutional Networks",
          authors: "Kipf & Welling",
          year: 2016,
          citations: 8,234,
          summary: "Semi-supervised classification with GCNs"
        }
      ]
    },
    {
      id: 2,
      name: "Recommendation Systems",
      icon: "🤖",
      count: 8,
      description: "Collaborative filtering research",
      papers: [
        {
          title: "Neural Collaborative Filtering",
          authors: "He et al.",
          year: 2017,
          citations: 2,456,
          summary: "Deep learning for collaborative filtering"
        }
      ]
    },
    {
      id: 3,
      name: "To Read",
      icon: "📈",
      count: 7,
      description: "Papers marked for future reading",
      papers: [
        {
          title: "Attention Is All You Need",
          authors: "Vaswani et al.",
          year: 2017,
          citations: 45,231,
          summary: "Transformer architecture for sequence modeling"
        }
      ]
    }
  ];

  const recommendations = [
    {
      title: "Graph Attention Networks",
      reason: "Based on your GNN interest",
      confidence: 0.92
    },
    {
      title: "Deep Residual Learning",
      reason: "Foundational deep learning work",
      confidence: 0.87
    },
    {
      title: "BERT: Pre-training Transformers",
      reason: "Related to your attention papers",
      confidence: 0.89
    }
  ];

  const renderFolders = () => (
    <div className="folders-view">
      <div className="stats-bar">
        <div className="stat">
          <span className="stat-number">47</span>
          <span className="stat-label">Papers</span>
        </div>
        <div className="stat">
          <span className="stat-number">8</span>
          <span className="stat-label">Folders</span>
        </div>
        <div className="stat">
          <span className="stat-number">12</span>
          <span className="stat-label">New</span>
        </div>
      </div>

      <div className="folders-list">
        {folders.map(folder => (
          <div 
            key={folder.id} 
            className="folder-item"
            onClick={() => {
              setSelectedFolder(folder);
              setViewMode('papers');
            }}
          >
            <div className="folder-icon">{folder.icon}</div>
            <div className="folder-info">
              <div className="folder-name">{folder.name}</div>
              <div className="folder-count">{folder.count} papers</div>
              <div className="folder-description">{folder.description}</div>
            </div>
            <div className="folder-arrow">›</div>
          </div>
        ))}
      </div>

      <div className="quick-actions">
        <button className="quick-action-btn">
          <span className="action-icon">📁</span>
          New Folder
        </button>
        <button className="quick-action-btn">
          <span className="action-icon">⭐</span>
          Starred
        </button>
      </div>
    </div>
  );

  const renderPapers = () => (
    <div className="papers-view">
      <div className="papers-header">
        <button 
          className="back-btn"
          onClick={() => setViewMode('folders')}
        >
          ← Back
        </button>
        <h2>{selectedFolder?.name}</h2>
        <button className="menu-btn">⋯</button>
      </div>

      <div className="papers-list">
        {selectedFolder?.papers.map((paper, index) => (
          <div key={index} className="paper-card">
            <div className="paper-header">
              <div className="paper-title">{paper.title}</div>
              <div className="paper-meta">
                {paper.authors} • {paper.year} • {paper.citations} citations
              </div>
            </div>
            <div className="paper-summary">{paper.summary}</div>
            <div className="paper-actions">
              <button className="action-btn primary">View</button>
              <button className="action-btn secondary">Remove</button>
            </div>
          </div>
        ))}
      </div>

      <div className="add-paper-btn">
        <button className="add-btn">
          <span className="add-icon">+</span>
          Add Paper
        </button>
      </div>
    </div>
  );

  const renderRecommendations = () => (
    <div className="recommendations-view">
      <div className="recommendations-header">
        <h2>AI Recommendations</h2>
        <div className="confidence-toggle">
          <span className="toggle-label">High Confidence</span>
          <div className="toggle-switch">
            <div className="toggle-slider"></div>
          </div>
        </div>
      </div>

      <div className="recommendations-list">
        {recommendations.map((rec, index) => (
          <div key={index} className="recommendation-card">
            <div className="recommendation-header">
              <div className="recommendation-title">{rec.title}</div>
              <div className="confidence-score">
                {Math.round(rec.confidence * 100)}%
              </div>
            </div>
            <div className="recommendation-reason">{rec.reason}</div>
            <div className="recommendation-actions">
              <button className="action-btn primary">Add to Library</button>
              <button className="action-btn secondary">Preview</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  return (
    <div className="personal-app">
      {/* Mobile Header */}
      <div className="mobile-header">
        <div className="header-left">
          <div className="user-avatar">MD</div>
          <div className="user-info">
            <div className="user-name">Madison Davis</div>
            <div className="user-status">Research Library</div>
          </div>
        </div>
        <div className="header-right">
          <button className="header-btn">🔍</button>
          <button className="header-btn">⚙️</button>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="nav-tabs">
        <button 
          className={`nav-tab ${viewMode === 'folders' ? 'active' : ''}`}
          onClick={() => setViewMode('folders')}
        >
          📁 Folders
        </button>
        <button 
          className={`nav-tab ${viewMode === 'recommendations' ? 'active' : ''}`}
          onClick={() => setViewMode('recommendations')}
        >
          💡 AI Recs
        </button>
      </div>

      {/* Main Content */}
      <div className="main-content">
        {viewMode === 'folders' && renderFolders()}
        {viewMode === 'papers' && renderPapers()}
        {viewMode === 'recommendations' && renderRecommendations()}
      </div>

      {/* Bottom Navigation */}
      <div className="bottom-nav">
        <button className="nav-item active">
          <span className="nav-icon">📚</span>
          <span className="nav-label">Library</span>
        </button>
        <button className="nav-item">
          <span className="nav-icon">🔍</span>
          <span className="nav-label">Search</span>
        </button>
        <button className="nav-item">
          <span className="nav-icon">📊</span>
          <span className="nav-label">Graph</span>
        </button>
        <button className="nav-item">
          <span className="nav-icon">👤</span>
          <span className="nav-label">Profile</span>
        </button>
      </div>
    </div>
  );
}

export default PersonalApp;
