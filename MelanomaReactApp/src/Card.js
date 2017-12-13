import React from 'react';
import {Card, CardMedia, CardTitle} from 'material-ui/Card';

const CardResults = (props) => (
    <Card>
        <CardMedia>
            <img src={props.image} alt="" />
        </CardMedia>
        <CardTitle 
            title="View Your Diagnosis After Uploading" 
            subtitle="Upload an image to see your classification results!" />
  </Card>
);

export default CardResults;