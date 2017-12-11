import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import Upload from './Upload';
import Card from './Card';

class App extends Component {

state = {imagestring: ""}
onimageupload = (imagestring) => {
	this.setState({imagestring : imagestring})
}	
  render() {
    return (
      	<div>
        	<MuiThemeProvider>
				<AppBar 
				style= {{'width': '100%'}} 
				title= "Melanoma Detection Web Service" 
				align ="center"
				showMenuIconButton={false}
				/>
				<Upload onupload = {this.onimageupload} />
				
				<Card image = {this.state.imagestring}/>
	  
			</MuiThemeProvider>
      </div>
    );
  }
}

export default App;
