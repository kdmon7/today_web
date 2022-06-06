import React from 'react';
import { Nav, NavLink } from 'reactstrap';
import { Link } from 'react-router-dom/cjs/react-router-dom';

import fashionPic from '../../assets/images/category/fashion.png';
import digitalPic from '../../assets/images/category/digital.png';
import booksPic from '../../assets/images/category/books.png';
import furniturePic from '../../assets/images/category/furniture.png';
import lifePic from '../../assets/images/category/life.png';

const Category = (props) => {
    return(
        <Nav>
            <Link>
                <div className="page-wrapper">
                    <div className="container-fluid">
                        <div className='p-t-10'>
                            <img src={fashionPic} alt="image" className='img-responsive img-rounded'></img>
                        </div>
                        <div className='p-t-10'>
                            <img src={digitalPic} alt="image" className='img-responsive img-rounded'></img>
                        </div>
                        <div className='p-t-10'>
                            <img src={booksPic} alt="image" className='img-responsive img-rounded'></img>
                        </div>
                        <div className='p-t-10'>
                            <img src={furniturePic} alt="image" className='img-responsive img-rounded'></img>
                        </div>
                        <div className='p-t-10'>
                            <img src={lifePic} alt="image" className='img-responsive img-rounded'></img>
                        </div>
                    </div>
                </div> 
            </Link>
            
        </Nav>
    );

}

export default Category;