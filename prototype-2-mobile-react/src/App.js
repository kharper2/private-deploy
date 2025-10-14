import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedTab, setSelectedTab] = useState('summary');
  const [isExpanded, setIsExpanded] = useState(false);

  const paperData = {
    title: "Graph Neural Networks for Recommendation Systems",
    authors: "Zhang et al.",
    year: 2023,
    venue: "ICML",
    citations: 127,
    abstract: "This paper presents a novel approach to recommendation systems using graph neural networks. We introduce a multi-layer GNN architecture that captures both local and global user-item interactions, achieving state-of-the-art performance on multiple datasets.",
    contributions: [
      "Novel GNN architecture for recommendation systems",
      "Solution to cold-start problem", 
      "State-of-the-art performance on benchmark datasets",
      "Open-source implementation available"
    ],
    relatedPapers: [
      {
        type: "Cited By",
        title: "Deep Learning for Collaborative Filtering",
        description: "Extends our work with attention mechanisms"
      },
      {
        type: "References", 
        title: "Graph Convolutional Networks",
        description: "Foundational work on GCNs"
      },
      {
        type: "Similar",
        title: "Neural Collaborative Filtering", 
        description: "Alternative neural network approach"
      }
    ],
    metrics: {
      impactScore: 4.2,
      reproducibility: 87,
      implementationReady: "High"
    }
  };

  return (
    <div className="app">
      {/* Mobile Header */}
      <div className="mobile-header">
        <button className="back-btn">←</button>
        <h1 className="mobile-title">Paper Details</h1>
        <button className="menu-btn">⋯</button>
      </div>

      {/* Paper Card */}
      <div className="paper-card">
        <div className="paper-header">
          <h2 className="paper-title">{paperData.title}</h2>
          <div className="paper-meta">
            <span className="author">{paperData.authors}</span>
            <span className="year">{paperData.year}</span>
            <span className="venue">{paperData.venue}</span>
          </div>
          <div className="citation-count">{paperData.citations} citations</div>
        </div>

        {/* Mobile Tabs */}
        <div className="mobile-tabs">
          <button 
            className={`tab ${selectedTab === 'summary' ? 'active' : ''}`}
            onClick={() => setSelectedTab('summary')}
          >
            Summary
          </button>
          <button 
            className={`tab ${selectedTab === 'related' ? 'active' : ''}`}
            onClick={() => setSelectedTab('related')}
          >
            Related
          </button>
          <button 
            className={`tab ${selectedTab === 'metrics' ? 'active' : ''}`}
            onClick={() => setSelectedTab('metrics')}
          >
            Metrics
          </button>
        </div>

        {/* Tab Content */}
        <div className="tab-content">
          {selectedTab === 'summary' && (
            <div className="summary-content">
              <div className="section">
                <h3>Abstract</h3>
                <p className={isExpanded ? 'expanded' : 'collapsed'}>
                  {paperData.abstract}
                </p>
                <button 
                  className="expand-btn"
                  onClick={() => setIsExpanded(!isExpanded)}
                >
                  {isExpanded ? 'Show Less' : 'Show More'}
                </button>
              </div>
              
              <div className="section">
                <h3>Key Contributions</h3>
                <ul className="contributions-list">
                  {paperData.contributions.map((contribution, index) => (
                    <li key={index}>{contribution}</li>
                  ))}
                </ul>
              </div>
            </div>
          )}

          {selectedTab === 'related' && (
            <div className="related-content">
              {paperData.relatedPapers.map((paper, index) => (
                <div key={index} className="related-paper">
                  <div className="paper-type">{paper.type}</div>
                  <h4 className="paper-title-small">{paper.title}</h4>
                  <p className="paper-description">{paper.description}</p>
                  <button className="view-paper-btn">View Paper →</button>
                </div>
              ))}
            </div>
          )}

          {selectedTab === 'metrics' && (
            <div className="metrics-content">
              <div className="metric-card">
                <div className="metric-value">{paperData.metrics.impactScore}</div>
                <div className="metric-label">Impact Score</div>
              </div>
              <div className="metric-card">
                <div className="metric-value">{paperData.metrics.reproducibility}%</div>
                <div className="metric-label">Reproducibility</div>
              </div>
              <div className="metric-card">
                <div className="metric-value">{paperData.metrics.implementationReady}</div>
                <div className="metric-label">Implementation Ready</div>
              </div>
            </div>
          )}
        </div>

        {/* Mobile Actions */}
        <div className="mobile-actions">
          <button className="action-btn primary">
            📥 Export
          </button>
          <button className="action-btn secondary">
            🔗 Share
          </button>
          <button className="action-btn secondary">
            💾 Save
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
