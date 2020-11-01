from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

icon = lambda fg='text', bg='dark', fontsize=40, text="?": widget.TextBox(
    **base(fg, bg),
    fontsize=30,
    text=text,
    padding=3
)

powerline = lambda fg="light", bg="dark": widget.TextBox(
   **base(fg, bg),
    text="", # Icon: nf-oct-triangle_left
    fontsize=40,
    padding=-2
)

workspaces = lambda: [
    separator(),
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=40,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    separator(),
    widget.WindowName(**base(fg='text'), fontsize=40, padding=5),
    separator(),
]

primary_widgets = [

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.80,),

    *workspaces(),

    icon(bg="color1", text=' '), # Icon: nf-fa-download

    separator(),
    
    widget.Pacman(**base(bg='color1'), update_interval=1800),

    separator(),

    icon(bg="color1", text=' ', fontsize=20,),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color1'), interface='enp2s0', format='{down}{up}', fontsize=20),

    widget.Systray(background=colors['color1'], padding=15, icon_size=35),
    
    widget.Clock(**base(bg='color1'), format=' %H:%M - %d/%m/%Y  '),

    

]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font',
    'fontsize': 40,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
