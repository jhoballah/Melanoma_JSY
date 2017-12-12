import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import Upload from './Upload';
import Card from './Card';
import axios from 'axios';

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
			image: this.state.imagestring
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
	if (this.state.imagestring !== undefined) {
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
				<Upload onupload = {this.onimageupload} />
				
				<Card 
					image = {this.state.imagestring} 
					sites = {this.state.sites} 
					classification = {this.state.results}/>
	  			
			</MuiThemeProvider>
      </div>
      

    );
  }
}

export default App;
