# dash-callback-chain

Dash component to visualize callback chains

## Usage

```python
import dash_callback_chain as chainvis

app.layout = html.Div([
    chainvis.CallbackChainVisualizer(id="chain"),
    #... your app ...
])

@app.callback( Output('chain', 'dot'), [Input('location', 'search')] )
def show_chain(s): return chainvis.dot_chain(app)

# ... the rest of your app's callbacks
```
