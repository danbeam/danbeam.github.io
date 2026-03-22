import React, { useRef, useState, useEffect } from 'react';
import './App.css';
import { MIXES } from './data/mixes';
import { Instagram, Disc, Cloud, ChevronLeft, ChevronRight } from 'lucide-react';

function App() {
  const sortedMixes = [...MIXES].sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  const carouselRef = useRef<HTMLDivElement>(null);
  const [canScrollLeft, setCanScrollLeft] = useState(false);
  const [canScrollRight, setCanScrollRight] = useState(false);

  const checkScroll = () => {
    const el = carouselRef.current;
    if (el) {
      setCanScrollLeft(el.scrollLeft > 5);
      setCanScrollRight(el.scrollLeft < el.scrollWidth - el.clientWidth - 5);
    }
  };

  useEffect(() => {
    checkScroll();
    window.addEventListener('resize', checkScroll);
    return () => window.removeEventListener('resize', checkScroll);
  }, []);

  const scroll = (direction: 'left' | 'right') => {
    const el = carouselRef.current;
    if (el) {
      const scrollAmount = 300;
      el.scrollBy({ left: direction === 'left' ? -scrollAmount : scrollAmount, behavior: 'smooth' });
    }
  };

  return (
    <div className="app">
      <header className="header">
        <div className="container">
          <div className="logo">funk the system</div>
        </div>
      </header>

      <main>
        <section id="bio" className="section bio-section">
          <div className="container">
            <h2 className="section-title">about</h2>
            <div className="bio-content">
              <p>funk the system (fts) is a DJ based in Los Angeles.</p>
              <p>(his boring, real world name is Dan Beam.)</p>
              <p>despite having "funk" in his name, fts plays all kinds of music. basically anything that's right for the time, place, and people.</p>
            </div>
          </div>
        </section>

        <section id="booking" className="section booking-section">
          <div className="container">
            <h2 className="section-title">booking & contact</h2>
            <div className="booking-info">
              <p><a href="mailto:bookings@fts.dj" className="email-link-inline">bookings@fts.dj</a></p>
            </div>
            <div className="social-links">
              <a href="http://instagram.com/djfunkthesystem" target="_blank" rel="noopener noreferrer" title="instagram">
                <Instagram size={32} />
              </a>
              <a href="https://www.mixcloud.com/funk-the-system" target="_blank" rel="noopener noreferrer" title="mixcloud">
                <Disc size={32} />
              </a>
              <a href="https://soundcloud.com/funk-the-system" target="_blank" rel="noopener noreferrer" title="soundcloud">
                <Cloud size={32} />
              </a>
            </div>
          </div>
        </section>

        <section id="mixes" className="section mixes-section">
          <div className="container">
            <h2 className="section-title">latest mixes</h2>
            <div className="carousel-wrapper">
              <button 
                className={`carousel-arrow left ${canScrollLeft ? 'active' : ''}`} 
                onClick={() => scroll('left')}
                disabled={!canScrollLeft}
              >
                <ChevronLeft size={32} />
              </button>
              
              <div className="carousel-container">
                <div 
                  className="mix-carousel" 
                  ref={carouselRef}
                  onScroll={checkScroll}
                >
                  {sortedMixes.map((mix) => (
                    <div key={mix.id} className="mix-card">
                      <div className="mix-art-container">
                        <img src={mix.picture} alt={mix.name} className="mix-art-img" />
                        {mix.duration && <div className="mix-duration">{mix.duration}</div>}
                      </div>
                      <h3>{mix.name}</h3>
                      <div className="mix-tags">
                        {mix.tags.map(tag => (
                          <span key={tag} className="tag">{tag}</span>
                        ))}
                      </div>
                      <div className="mix-actions">
                        {mix.mixcloudUrl && (
                          <a href={mix.mixcloudUrl} target="_blank" rel="noopener noreferrer" className="listen-link mc">
                            Listen on Mixcloud
                          </a>
                        )}
                        {mix.soundcloudUrl && (
                          <a href={mix.soundcloudUrl} target="_blank" rel="noopener noreferrer" className="listen-link sc">
                            Listen on Soundcloud
                          </a>
                        )}
                        {mix.spotifyUrl && (
                          <a href={mix.spotifyUrl} target="_blank" rel="noopener noreferrer" className="listen-link sp">
                            Tracks on Spotify
                          </a>
                        )}
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              <button 
                className={`carousel-arrow right ${canScrollRight ? 'active' : ''}`} 
                onClick={() => scroll('right')}
                disabled={!canScrollRight}
              >
                <ChevronRight size={32} />
              </button>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer">
        <div className="container">
          <p>&copy; 2026 funk the system. all rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
