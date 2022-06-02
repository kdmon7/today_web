import React from "react";
import PropTypes from "prop-types";



// core components
import Header from "../../components/header/header.jsx";
import HeaderBanner from "../../components/banner/banner.jsx";
import Footer from "../../components/footer/footer.jsx";

// sections for this page
import Buttons from "./sections/buttons.jsx";
import Labels from "./sections/labels.jsx";
import PagePagination from "./sections/pagination.jsx";
import Images from "./sections/images.jsx";
import Breadcrumbs from "./sections/breadcrumbs.jsx";
import Cards from "./sections/cards.jsx";
import Dropdowns from "./sections/dropdowns.jsx";
import PageForm from "./sections/form.jsx";
import PageTable from "./sections/table.jsx";
import Notification from "./sections/notification.jsx";
import TooltipPopover from "./sections/tooltip-popover.jsx";
import Typography from "./sections/typography.jsx";
import JsComponents from "./sections/js-components.jsx";
import CallToAction from "../../components/call-to-action/CallToAction"


const Components = () => {
    return (
        <div id="main-wrapper">
            <Header />
            <div className="page-wrapper">
                <div className="container-fluid">
                    <HeaderBanner />
                </div>
            </div>
        </div>
    );
}

Components.propTypes = {
    classes: PropTypes.object
};

export default Components;
