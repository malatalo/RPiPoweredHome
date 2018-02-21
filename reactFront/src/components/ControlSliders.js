import React, {Component} from 'react';
import Slider from 'material-ui/Slider';
import Toggle from 'material-ui/Toggle';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const styles = {
  root: {
    marginTop:30,
    paddingTop:30,
    display: 'flex',
    height: 150,
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'flex-start',
  },
  textRow: {
    width:200,
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'flex-start',
    justifyContent: 'space-between',
  },
  toggleRow: {
    width:150,
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'flex-start',
    justifyContent: 'space-around',
  },
  sliders: {
    width: 200,
    height: 75,
  },
  block: {
    maxWidth: 250,
  },
  toggle: {
    marginBottom: 16,
  },
  thumbOff: {
    backgroundColor: '#000',
  },
  trackOff: {
    backgroundColor: '#9E9E9E',
  },
  thumbSwitched: {
    backgroundColor: '#000',
  },
  trackSwitched: {
    backgroundColor: '#9E9E9E',
  },
};

const brightSliderTheme = getMuiTheme({
  slider: {
    selectionColor: 'black',
    handleFillColor: 'black',
  }
});

export default class ControlSliders extends Component {
  state = {
    redColor: 0,
    greenColor: 0,
    blueColor: 0,
  };
  
  
  
  render() {
    return (
      <div style={styles.root}>
        <div style={styles.textRow}>
          <span>Brightness</span>
          <span>{this.props.brightness}%</span>
        </div>
        <MuiThemeProvider muiTheme={brightSliderTheme}>
          <Slider 
            style={styles.sliders} 
            axis="x" 
            min={0}
            max={100}
            step={5}
            value={this.props.brightness}
            onChange={this.props.handleBrightnessChange}
          />
        </MuiThemeProvider>
      <div style={styles.toggleRow}>
          <span style={{marginTop:2.5}}>1s</span>
          <Toggle
            style={{width:20}}
            thumbStyle={styles.thumbOff}
            trackStyle={styles.trackOff}
            thumbSwitchedStyle={styles.thumbSwitched}
            trackSwitchedStyle={styles.trackSwitched}
            labelStyle={styles.labelStyle}
            onToggle={this.props.handleToggle}
            toggled={this.props.toggleTime}
          />
        <span style={{marginTop:2.5}}>&nbsp;60s</span>
        </div>
      </div>
    )
  }
}