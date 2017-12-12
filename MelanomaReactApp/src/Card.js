import React from 'react';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import {
  Table,
  TableBody,
  TableHeader,
  TableHeaderColumn,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';

const CardResults = (props) => (

    <Card>
    
    
        
    <CardMedia
        
    >
        <img src={props.image} alt="" />
    </CardMedia>
    <CardTitle 
        title="View Your Diagnosis After Uploading" 
        subtitle="Upload an image to see your classification results!" />
    <CardText>
        
    </CardText>
    
  </Card>
);

export default CardResults;