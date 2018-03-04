import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Viz from 'viz.js'

/**
 * CallbackChainVisualizer helps you visualize your callback chain.
 * The `dot` property should be the output of the built-in `dot_chain`
 * Python function.
 */
export default class CallbackChainVisualizer extends Component {
    render() { return (
          <details>
            <summary>show callback chain</summary>
            <div dangerouslySetInnerHTML={{__html: Viz(this.props.dot, {format: 'svg'})}} />
          </details>); }
}

CallbackChainVisualizer.defaultProps = {
    dot: ''
};

CallbackChainVisualizer.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * A description of the callback chain in the DOT language
     */
    dot: PropTypes.string
};
