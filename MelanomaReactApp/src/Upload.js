import React, { Component } from 'react';
import { UploadField } from '@navjobs/upload';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';



class Upload extends Component {
    constructor() {
        super();
	this.state = {
	    currentImageString: '',
    }
}
    onUpload = (files) => { 
	const reader = new FileReader();
	const file = files [0];
	reader.readAsDataURL(file);
	reader.onloadend = () => {
	      
	    console.log(reader.result);
    	    this.setState({currentImageString: reader.result});	
    	    this.props.onupload(reader.result)
        }
    }

    render() {
	
        return (

             <div>
             
	     	 	<h2 align="center" > Upload Your Image Below</h2> 
	     	 	
             	<UploadField onFiles={this.onUpload}>
  		    			<div style= {{ 
						backgroundColor: 'gray',
						opacity : '0.3',
			 			height: '300px',
						textAlign: 'center'}}>
					Click This Box Or Drag Your Image To Upload
		    		</div>
	         	</UploadField>
	    <center>		
			<img
				style={{height: undefined, width:undefined}}
				src={this.state.currentImageString} 
				resizeMode="contain"
				alt="Your Image Will Be Rendered Below!" 
				align="center"
			/>
		</center>
	    </div>
        )
    }
}
export default Upload;