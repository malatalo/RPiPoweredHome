import React, {Component} from 'react';
import Slider from 'material-ui/Slider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const styles = {
  root: {
    width: '100%',
    display: 'flex',
    height: 200,
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
  },
  sliders: {
    width: 200,
    height: 50,
  },
  slidersSection: {
    width:300,
    height: 1,
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom:50,
  },
  sliderValueSection: {
    width:350,
    height: 1,
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
};

const redSliderTheme = getMuiTheme({
  slider: {
    selectionColor: '#EF5350',
    handleFillColor: '#EF5350',
  }
});

const greenSliderTheme = getMuiTheme({
  slider: {
    selectionColor: '#81C784',
    handleFillColor: '#81C784',
  }
});

const blueSliderTheme = getMuiTheme({
  slider: {
    selectionColor: '#039BE5',
    handleFillColor: '#039BE5',
  }
});


export default class ColorSliders extends Component {
  
  //OH GOD PLS LOOK AWAY
  //JUST THINK OF THE CHILDREN
  render() {
    return (
      <div style={styles.root}>
        <div style={styles.sliderValueSection}>
          <span className="sliderSpan">Red&nbsp;</span>
          <span className="sliderSpan">&nbsp;{this.props.redColor}</span>
        </div>
        <div style={styles.slidersSection}>
          <MuiThemeProvider muiTheme={redSliderTheme}>
            <Slider 
              style={styles.sliders} 
              axis="x" 
              min={0}
              max={255}
              step={1}
              value={this.props.redColor}
              onChange={(e,v)=>this.props.handleColorChange(e,v,"redColor")}
            />
          </MuiThemeProvider>
        </div>
        <div style={styles.sliderValueSection}>
          <span className="sliderSpan">Green&nbsp;</span>
          <span className="sliderSpan">{this.props.greenColor}</span>
        </div>
        <div style={styles.slidersSection}>
          <MuiThemeProvider muiTheme={greenSliderTheme}>
            <Slider 
              style={styles.sliders}
              axis="x" 
              min={0}
              max={255}
              step={1}
              value={this.props.greenColor}
              onChange={(e,v)=>this.props.handleColorChange(e,v,"greenColor")}
              />
          </MuiThemeProvider>
        </div>
        <div style={styles.sliderValueSection}>
            <span className="sliderSpan">Blue&nbsp;</span>
          <span className="sliderSpan">{this.props.blueColor}</span>
        </div>
        <div style={styles.slidersSection}>
          <MuiThemeProvider muiTheme={blueSliderTheme}>
            <Slider 
              style={styles.sliders}
              axis="x" 
              min={0}
              max={255}
              step={1}
              value={this.props.blueColor}
              onChange={(e,v)=>this.props.handleColorChange(e,v,"blueColor")}
              />
          </MuiThemeProvider>
        </div>
      </div>
    )
  }
}