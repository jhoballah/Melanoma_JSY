import React, { Component } from 'react';
import { UploadField } from '@navjobs/upload';

class Upload extends Component {
    constructor() {
        super();
}   
    onUpload = (files) => { 
		if (files[0] !== undefined){
			const reader = new FileReader();
			const file = files[0];
			reader.readAsDataURL(file);
			reader.onloadend = () => {  
			    console.log(reader.result); 
		    	this.props.onupload(reader.result);
		    	this.props.headerlessupload(reader.result.substr(reader.result.indexOf(',') + 1));
		        }
		    }
    }
    render() {
        return (
             <div>
	     	 	<h2 align="center" > Upload Your .JPG Image Below</h2>      	 	
             	<UploadField onFiles={this.onUpload}>
		    		<div style= {{ 
						backgroundColor: 'gray',
						opacity : '0.3',
			 			height: '300px',
						textAlign: 'center'}}>
						Click This Box Or Drag Your .JPG Image To Upload It
		    		</div>
	         	</UploadField>
	    </div>
        )
    }
}

export default Upload;
