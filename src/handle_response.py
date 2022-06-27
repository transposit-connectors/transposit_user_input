def handle_response(inputs):
    custom_output_params = {
        "outputs": inputs["input_results"]
    }
    return workflow.log.done("Action completed successfully", {}, custom_output_params)