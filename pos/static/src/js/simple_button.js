/** Import necessary modules from Odoo POS */
import { Component } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { TextInputPopup } from "@point_of_sale/app/utils/input_popups/text_popup";
import { useState } from "@odoo/owl";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";

/** SampleButton Component */
class SampleButton extends Component {
    setup() {
        super.setup();
        // Local state to manage the popup input value
        this.state = useState({
            note: "",
        });
    }

    async onSampleButtonClick() {
        // Show the popup to enter a note
        const { confirmed, payload } = await this.showPopup(TextInputPopup, {
            title: _t("Add Notes"),
            startingValue: this.state.note, // Set initial value as state.note
            placeholder: _t("Enter your notes here..."),
        });

        if (confirmed) {
            this.state.note = payload;  // Update the note in the state
            this.showNotification(_t("Note added successfully."));
        }
    }
}

SampleButton.template = "pos_sample_button.SampleButton";  // Link to the button template

/** Add the custom button to PaymentScreen */
PaymentScreen.addControlButton({
    component: SampleButton,
    label: _t("Sample Button"),
    className: "sample-button",
    onClick: "onSampleButtonClick",
});
