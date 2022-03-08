import React, { Component } from 'react';
import './styles/Navigation_style.css';
import { NavLink } from 'react-router-dom';
import { Navbar, Nav, Container, NavDropdown } from 'react-bootstrap'


function Navigation() {
    return (
        <div className='Navigation_container'>
            <Navbar bg="dark" expand="lg">
                <Container>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <NavLink className="d-inline p-2 bg-dark text-white nav_link" to="/">Home</NavLink>
                            <NavLink className="d-inline p-2 bg-dark text-white nav_link" to="/Department">Department</NavLink>
                            <NavLink className="d-inline p-2 bg-dark text-white nav_link" to="/Employee">Employee</NavLink>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </div>
    )
}

export default Navigation;
