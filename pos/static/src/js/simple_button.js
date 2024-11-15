odoo.define('pos_custom_button.CustomButton', function (require) {
    "use strict";
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class CustomButton extends PosComponent {
        async onClick() {
            // Action triggered when button is clicked
            alert('Custom Button Clicked!');
        }
    }

    CustomButton.template = 'CustomButton';
    Registries.Component.add(CustomButton);
    return CustomButton;
});