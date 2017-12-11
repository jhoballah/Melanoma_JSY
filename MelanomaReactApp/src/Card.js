import React from 'react';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';


const CardResults = (props) => (

    <Card>
    
    <CardHeader/>

        
    <CardMedia
        overlay={<CardTitle title="Uploaded Image" />}
    >
        <img src={props.image} alt="" />
    </CardMedia>
    <CardTitle 
        title="Diagnosis Results" 
        subtitle="Your Classification Can Be Seen Below" />
    <CardText>
        
    </CardText>
    
  </Card>
);

export default CardResults;