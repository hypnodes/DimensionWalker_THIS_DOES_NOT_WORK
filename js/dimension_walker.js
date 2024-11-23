import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "DimensionWalker",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "DimensionWalker") {
            // Store original onExecuted
            const onExecuted = nodeType.prototype.onExecuted;

            // Override onExecuted to handle dynamic outputs
            nodeType.prototype.onExecuted = function(message) {
                const dimensions = this.widgets.find(w => w.name === "dimensions").value;

                // Update outputs based on dimensions
                this.outputs = [];
                for (let i = 0; i < dimensions; i++) {
                    this.addOutput(`coord${i + 1}`, "FLOAT");
                }

                if (onExecuted) {
                    onExecuted.apply(this, arguments);
                }
            };

            // Handle widget changes
            const onWidgetChanged = nodeType.prototype.onWidgetChanged;
            nodeType.prototype.onWidgetChanged = function(name, value) {
                if (name === "dimensions") {
                    // Update outputs when dimensions change
                    this.outputs = [];
                    for (let i = 0; i < value; i++) {
                        this.addOutput(`coord${i + 1}`, "FLOAT");
                    }
                }

                if (onWidgetChanged) {
                    onWidgetChanged.apply(this, arguments);
                }
            };
        }
    }
});
