export function MotdContent() {
  return (
    <div className="container">
      <div className="title">
        <div className="title-border">
          <div className="title-text">MYTHOS MUD</div>
          <div className="title-subtitle">Welcome to the Dreamlands</div>
        </div>
      </div>

      <div className="yellow-sign">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~
        <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ &nbsp;\
        <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;( &nbsp;&nbsp;)
        <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ &nbsp;@ &nbsp;\
        <br />
        &nbsp;&nbsp;&nbsp;&nbsp;/ &nbsp;&nbsp;| &nbsp;&nbsp;\
        <br />
        &nbsp;&nbsp;&nbsp;( &nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp;)
        <br />
        &nbsp;&nbsp;&nbsp;\ &nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp;/
        <br />
        &nbsp;&nbsp;&nbsp;&nbsp;\ &nbsp;&nbsp;| &nbsp;&nbsp;/
        <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\ &nbsp;| &nbsp;/
        <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\ | /
        <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* &nbsp;&nbsp;&nbsp;*
        <br />
      </div>

      <div className="welcome-text">
        <p>
          Greetings, seeker of forbidden knowledge! You stand at the threshold of realities beyond mortal comprehension.
        </p>

        <p>
          As noted in the restricted archives of Miskatonic University, this realm exists at the intersection of waking
          consciousness and the eldritch dimensions that lie just beyond human perception. The Yellow Sign you see above
          serves as both warning and invitation.
        </p>

        <p>
          Remember: what you encounter here may challenge your understanding of reality itself. The boundaries between
          planes are thin, and the entities that dwell in the spaces between spaces are ever-watchful.
        </p>
      </div>

      <div className="warning">
        ⚠️ WARNING: Prolonged exposure to eldritch knowledge may result in temporary or permanent alterations to your
        perception of reality. Proceed with caution. ⚠️
      </div>

      <div className="stats">
        <h3>Current Realm Status</h3>
        <p>
          <strong>Active Players:</strong> [Dynamic]
        </p>
        <p>
          <strong>Known Zones:</strong> Arkham City, Innsmouth, Katmandu
        </p>
        <p>
          <strong>Reality Stability:</strong> 87.3% (Within Acceptable Parameters)
        </p>
        <p>
          <strong>Dimensional Rifts:</strong> 2 (Minor, Under Observation)
        </p>
      </div>

      <div className="welcome-text">
        <p>
          <strong>Available Commands:</strong>
        </p>
        <p>
          • <code>look</code> - Examine your surroundings
        </p>
        <p>
          • <code>move [direction]</code> - Navigate between locations
        </p>
        <p>
          • <code>inventory</code> - Check your possessions
        </p>
        <p>
          • <code>stats</code> - View your character statistics
        </p>
        <p>
          • <code>help</code> - Access the knowledge archives
        </p>
      </div>

      <div className="footer">
        <p>Miskatonic University - Department of Occult Studies</p>
        <p>"That is not dead which can eternal lie, and with strange aeons even death may die."</p>
        <p>Connection established via eldritch protocols | Last updated: [Timestamp]</p>
      </div>
    </div>
  );
}
