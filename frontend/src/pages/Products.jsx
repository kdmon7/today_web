import React from 'react';
import Category from '../views/components/Category';

const Products = (props) => {
    return(
        <div id="main-wrapper">
            <div className="page-wrapper" >
                <Category/>
            </div>
        </div>
    );
}

export default Products;