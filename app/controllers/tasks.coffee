class Tasks extends Spine.Controller
    events:
        "change     input[type=checkbox]":  "toogle"
        "click      .destroy":              "remove"
        "dbclick    .view":                 "edit"
        "keypress   input[type=text]":      "blurOnEnter"
        "blur       input[type=text]":      "close"

    elements:
        "input[type=text]": "input"

    constructor: ->
        super
        @item.bind("update", @render)
        @item.bind("destroy", @release)

    render: =>
        @replace($("#taskTemplate").tmpl(@item))
        @

    toogle: ->
        @item.done = !@item.done
        @item.save()

    remove: ->
        @item.destroy()

    edit: ->
        @el.addClass("editing")
        @input.focus()

    blurOnEnter: (e) ->
        if e.keyCode is 13 then e.target.blur()

    close: ->
        @el.removeClass("editing")
        @item.updateAttributes({name: @input.val()})

module.exports = Tasks