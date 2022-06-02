import React from 'react';
import { HashLink as Link } from 'react-router-hash-link';
import { Container, Row, Col } from 'reactstrap';

const HeaderBanner = () => {
    return (
        <div className="static-slider-head">
            <Container>
                <Row className="justify-content-center">
                    <Col lg="8" md="6" className="align-self-center text-center">
                        <h3 className="subtitle font-bold" color='#ffffff'>중고거래도 이젠<br /> 쉽게, 안전하게!</h3>
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default HeaderBanner;
