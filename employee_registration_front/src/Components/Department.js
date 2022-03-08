import React, { Component } from 'react';


export default class Department extends Component {

    constructor(props){
        super(props);
        this.state = {deps:[]}
    }

    RefreshList(){
        fetch(process.env.REACT_APP_API+'department')
        .then(response=>response.json())
        .then(data=>{
            this.setState({deps:data});
        });
    }

    componentDidMount(){
        this.RefreshList();
    }

    componentDidUpdate(){
        this.refreshList();
    }

    render(){
        const {deps} = this.state; 
        return (
            <div className='Department_container'>
                
            </div>
        )
    }
}
