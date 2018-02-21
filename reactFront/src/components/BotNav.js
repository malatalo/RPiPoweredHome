import React, {Component} from 'react';
import FontIcon from 'material-ui/FontIcon';
import {BottomNavigation, BottomNavigationItem} from 'material-ui/BottomNavigation';
import Paper from 'material-ui/Paper';

const favoritesIcon = <FontIcon className="material-icons">settings_backup_restore</FontIcon>;
const cachedIcon = <FontIcon className="material-icons">cached</FontIcon>;

export default class BotNav extends Component {

  render() {
    return (
      <div>
        <Paper zDepth={2}>
          <BottomNavigation style={{position: "fixed", bottom:"0", width:"100%"}}>          
            <BottomNavigationItem
              label="Current"
              icon={cachedIcon}
              onClick={() => this.props.setDefaults()}
            />
            <BottomNavigationItem
              label="Default"
              icon={favoritesIcon}
              onClick={() => this.props.fetchCurrent()}
            />
            
          </BottomNavigation>
        </Paper>
      </div>
    );
  }
}