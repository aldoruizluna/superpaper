"""Error etc. info dialog."""

import sys

# Try to import wx, but don't fail if it's not available
try:
    import wx
    WX_AVAILABLE = True
except ImportError:
    WX_AVAILABLE = False

def show_message_dialog(message, msg_type="Info", parent=None, style="OK"):
    """General purpose info dialog in GUI mode, falls back to console in CLI mode."""
    # Type can be 'Info', 'Error', 'Question', 'Exclamation'
    
    if not WX_AVAILABLE:
        # Fallback to console output when wx is not available
        prefix = f"[{msg_type}]"
        print(f"{prefix} {message}", file=sys.stderr if msg_type == "Error" else sys.stdout)
        if style == "YES_NO":
            # In CLI mode, we can't really ask for input, so return False
            print("(Interactive dialog not available in CLI mode, defaulting to 'No')")
            return False
        return
    
    if style == "OK":
        dial = wx.MessageDialog(parent, message, msg_type, wx.OK|wx.STAY_ON_TOP|wx.CENTRE)
        dial.ShowModal()
    elif style == "YES_NO":
        dial = wx.MessageDialog(parent, message, msg_type, wx.YES_NO|wx.STAY_ON_TOP|wx.CENTRE)
        res = dial.ShowModal()
        if res == wx.ID_YES:
            return True
        else:
            return False
