import React, { Component } from 'react';

import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import Upload from './Upload';
import Card from './Card';
import axios from 'axios';
import Table from './Table'

class App extends Component {

state = {
	'classification':''
    }

    getClassification = () => {

        axios({
			method: 'post',
			url: 'http://vcm-1856.vm.duke.edu:5900/WebAppMelanomaData',
			data: {
			image: [this.state.headerlessimage]
			}
		})
        .then( (results) =>{
        	console.log(results);
        	console.log("The classification results");
        	console.log(results.data)
        	this.setState({'classification': results.data})
        })
    };

state = {imagestring: ""}
onimageupload = (imagestring) => {
	this.setState({imagestring : imagestring})
	
}

state = {headerlessimage: ""}
onheaderlessupload = (headerlessimage) => {
	this.setState({headerlessimage : headerlessimage})
	if (this.state.headerlessimage !== undefined) {
		this.getClassification()
	}
	
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
			</MuiThemeProvider>
			<MuiThemeProvider>
				<Upload 
					onupload = {this.onimageupload}
					headerlessupload = {this.onheaderlessupload} 
				/>
			</MuiThemeProvider>
			<MuiThemeProvider>	
				<Card 
					image = {this.state.imagestring} 
				/>
			</MuiThemeProvider>
			<MuiThemeProvider>
				<Table classification = {this.state.classification}  />
	  				
			</MuiThemeProvider>
      </div>
      

    );
  }
}

export default App;
