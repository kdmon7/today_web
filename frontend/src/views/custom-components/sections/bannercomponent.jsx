/* eslint-disable */
import React from 'react';
import { Row, Col, Container } from 'reactstrap';

const BannerComponent = () => {
    return (
        <div>
            <div className="spacer">
                <Container>
                    <Row className="justify-content-center">
                        <Col md="7" className="text-center">
                            <h1 className="title font-bold">Banners</h1>
                            <h6 className="subtitle">Here you can check Demos we created based on WrapKit. Its quite easy to Create your own dream website &amp; dashboard in No-time.</h6>
                        </Col>
                    </Row>
                </Container>
            </div>
            <div className="static-slider10">
                <Container>
                    <Row className="justify-content-center">
                        <Col md="6" className="align-self-center text-center">
                            <span className="label label-rounded label-inverse">Creating Brands</span>
                            <h1 className="title">ONE BILLON People Use Facebook</h1>
                            <h6 className="subtitle op-8">Pellentesque vehicula eros a dui pretium ornare. Phasellus congue vel quam nec luctus.In accumsan at eros in dignissim. Cras sodales nisi nonn accumsan.</h6>
                            <a className="btn btn-outline-light btn-rounded btn-md btn-arrow m-t-20" data-toggle="collapse" href=""><span>Do you Need Help? <i className="ti-arrow-right"></i></span></a>
                        </Col>
                    </Row>
                </Container>
            </div>
            <div className="static-slider3">
                <Container>
                    <Row className="justify-content-center">
                        <Col md="8" className="align-self-center text-center">
                            <h1 className="title">I’m Johanthan Doe, an <b className="font-bold">Entreprenuer, Designer & Front-end Developer</b>, Making <span className="text-success-gradiant font-bold typewrite" data-period="2000" data-type='[ "Photoshop", "Web Application", "Web Designing", "Web Development" ]'></span></h1>
                            <a className="btn btn-success-gradiant btn-md btn-arrow m-t-20" data-toggle="collapse" href=""><span>Checkout My Work <i className="ti-arrow-right"></i></span></a>
                        </Col>
                    </Row>
                </Container>
            </div>
        </div>
    );
}

export default BannerComponent;
