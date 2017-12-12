import React from 'react';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';


const CardResults = (props) => (

    <Card>
    
    
        
    <CardMedia
        
    >
        <img src={props.image} alt="" />
    </CardMedia>
    <CardTitle 
        title="View Your Diagnosis After Uploading" 
        subtitle="Your Classification Can Be Seen Below" />
    <CardText>
        {(props.sites !== undefined) ? props.results : "To view your classification results, you must upload an image."}
    </CardText>
    
  </Card>
);

export default CardResults;