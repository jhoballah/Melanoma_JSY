import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import Upload from './Upload';
import Card from './Card';
import axios from 'axios';
import Table from './Table'

class App extends Component {

state = {
	'sites': '',
	'classification':''
    }

    getData = () => {
    	
        axios.get('http://adpl.suyash.io/api/sites').then( (data) => {
            console.log(data);
            console.log("The sites data is");
            console.log(data.data)
            this.setState({'sites': data.data});
            
        
        });

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
		this.getData()

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
				<Upload 
				onupload = {this.onimageupload}
				headerlessupload = {this.onheaderlessupload} />
				
				<Card 
					image = {this.state.imagestring} 
					sites = {this.state.sites} 
					classification = {this.state.classification}/>

				<Table  displayRowCheckbox = {false} classification = {this.state.classification}  />
	  				
			</MuiThemeProvider>
      </div>
      

    );
  }
}

export default App;
