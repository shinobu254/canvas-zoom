import gradio as gr
from modules import shared

shared.options_templates.update(shared.options_section(('canvas_zoom', "Canvas Zoom"), {
    "canvas_hotkey_zoom": (shared.OptionInfo("Shift", "Zoom canvas", gr.Radio, {"choices": ["Shift","Ctrl", "Alt"]}).info("If you choose 'Shift' you cannot scroll horizontally, 'Alt' can cause a little trouble in firefox") if (info := getattr(shared.OptionInfo("Alt", "Zoom canvas", gr.Radio, {"choices": ["Shift","Ctrl", "Alt"]}), 'info', None)) else shared.OptionInfo("Alt", "Zoom canvas", gr.Radio, {"choices": ["Shift","Ctrl", "Alt"]})),
    "canvas_hotkey_adjust": (shared.OptionInfo("Ctrl", "Adjust brush size", gr.Radio, {"choices": ["Shift","Ctrl", "Alt"]}).info("If you choose 'Shift' you cannot scroll horizontally, 'Alt' can cause a little trouble in firefox") if (info := getattr(shared.OptionInfo("Ctrl", "Adjust brush size", gr.Radio, {"choices": ["Shift","Ctrl", "Alt"]}), 'info', None)) else shared.OptionInfo("Ctrl", "Adjust brush size", gr.Radio, {"choices": ["Shift","Ctrl", "Alt"]})),
    "canvas_zoom_undo_extra_key": (shared.OptionInfo("Ctrl", "Extra key to undo", gr.Radio, {"choices": ["Shift","Ctrl", "Alt","None"]}).info("You select extra key for combination to 'undo the action', if you select None, the 'undo' will be only on the hotkey.") if (info := getattr(shared.OptionInfo("Ctrl", "Extra key to undo", gr.Radio, {"choices": ["Shift","Ctrl", "Alt","None"]}), 'info', None)) else shared.OptionInfo("Ctrl", "Extra key to undo size", gr.Radio, {"choices": ["Shift","Ctrl", "Alt","None"]})),
    "canvas_zoom_hotkey_undo": shared.OptionInfo("Z", "Undo last action"),
    "canvas_hotkey_move": shared.OptionInfo("F", "Moving the canvas"),
    "canvas_hotkey_fullscreen": shared.OptionInfo("S", "Fullscreen Mode, maximizes the picture so that it fits into the screen and stretches it to its full width "),
    "canvas_hotkey_reset": shared.OptionInfo("R", "Reset zoom and canvas positon"),
    "canvas_zoom_inc_brush_size": shared.OptionInfo("]", "Increase brush size"),
    "canvas_zoom_dec_brush_size": shared.OptionInfo("[", "Decrease brush size"),
    "canvas_zoom_hotkey_open_colorpanel": shared.OptionInfo("Q", "Quickly open the color panel"),
    "canvas_zoom_hotkey_pin_colorpanel": shared.OptionInfo("T", "Attach the color panel to the mouse "),
    "canvas_zoom_hotkey_dropper": shared.OptionInfo("A", "Toggle dropper ( Works in Sketch and Inpaint Sketch )"),
    "canvas_zoom_hotkey_fill": shared.OptionInfo("X", "Fill the canvas with brush color ( works in sketch/inpaint sketch )"),
    "canvas_zoom_hotkey_transparency": shared.OptionInfo("C", "Activate transparency mode (works only in Inpaint)"),
    "canvas_hotkey_overlap": shared.OptionInfo("O", "Toggle overlap ( Technical button, neededs for testing )"),
    "canvas_show_tooltip": shared.OptionInfo(True, "Enable tooltip on the canvas"),
    "canvas_zoom_hide_btn": shared.OptionInfo(True, "Hide the control buttons when you draw"),
    "canvas_zoom_mask_clear": shared.OptionInfo(True, "Enable mask clearing in inpaint after any picture is moved in inpaint via buttons"),
    "canvas_auto_expand": shared.OptionInfo(True, "Automatic expansion of an image that does not fit completely within the canvas area, similar to manual S and R entry"),
    "canvas_zoom_enable_integration": shared.OptionInfo(True, "Enable integration with ControlNet, Regional Prompter and Latent Couple(Two Shot), Inpaint Anything"),
    "canvas_zoom_brush_size": shared.OptionInfo(200, "Increase % of the maximum brush size", gr.Slider, {"minimum": 100, "maximum": 1000, "step": 50}),
    "canvas_zoom_transparency_level": shared.OptionInfo(70, "Opacity level in inpaint.Works with panel 1.6 otherwise this setting will adjust the transparency in transparency mode from the extension", gr.Slider, {"minimum": 10, "maximum": 100, "step": 5}),
    "canvas_zoom_brush_opacity": shared.OptionInfo(False, "Makes the brush the same transparency as the mask"),
    # "canvas_zoom_inpaint_prevent_work": shared.OptionInfo(False, "Always prevent inpainting models work on txt2img tab by default"), #TODO
    "canvas_zoom_inpaint_label": shared.OptionInfo(True, "INPAINT - Show the label next to the model selection when you select an inpaint model"),
    "canvas_zoom_inpaint_warning": shared.OptionInfo(True, "INPAINT - Show warning when you try to use inpaint model in txt2img mode(The model name must contain 'inpainting' or 'inpaint'.)"),
    "canvas_zoom_inpaint_change_btn_color": shared.OptionInfo(False, "INPAINT - Enable button color change when inpaint model is selected"),
    "canvas_zoom_inpaint_btn_color": shared.OptionInfo("#C33227", 'INPAINT - Change the color of the button, which will change if the inpaint model is selected.',gr.ColorPicker),
    "canvas_zoom_brush_outline": shared.OptionInfo(False, "Enable outline for the brush"),
    "canvas_zoom_add_buttons": shared.OptionInfo(False, "Add a button to switch to full screen mode. May be useful for devices without keyboard"),
    "canvas_blur_prompt": shared.OptionInfo(False, "Take the focus off the prompt when working with a canvas"),
    "canvas_zoom_draw_staight_lines": shared.OptionInfo(False, "Enable the function of drawing straight lines between points while holding down the Shift key"),
    "canvas_zoom_inpaint_brushcolor": shared.OptionInfo("#000000", 'Change the default inpaint brush color. Since version 1.6 this setting doesnt work, look for it in "img2img" in the settings .',gr.ColorPicker),
    "canvas_zoom_disabled_functions": shared.OptionInfo(["Overlap"], "Disable function that you don't use", gr.CheckboxGroup, {"choices": ["Zoom","Adjust brush size","Undo", "Moving canvas","Fullscreen","Reset Zoom","Overlap","Open color panel","Pin color panel","Dropper","Fill","Transparency Mode"]}),
}))
