def execute(inputs):
    api.log(inputs["input_form_blocks"])
    task.create("this.handle_response", {}).continueAfterUserInput(inputs["input_form_blocks"])
