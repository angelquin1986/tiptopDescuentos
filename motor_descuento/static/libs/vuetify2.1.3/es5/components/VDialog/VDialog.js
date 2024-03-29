"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

require("../../../src/components/VDialog/VDialog.sass");

var _activatable = _interopRequireDefault(require("../../mixins/activatable"));

var _dependent = _interopRequireDefault(require("../../mixins/dependent"));

var _detachable = _interopRequireDefault(require("../../mixins/detachable"));

var _overlayable = _interopRequireDefault(require("../../mixins/overlayable"));

var _returnable = _interopRequireDefault(require("../../mixins/returnable"));

var _stackable = _interopRequireDefault(require("../../mixins/stackable"));

var _toggleable = _interopRequireDefault(require("../../mixins/toggleable"));

var _clickOutside = _interopRequireDefault(require("../../directives/click-outside"));

var _helpers = require("../../util/helpers");

var _ThemeProvider = _interopRequireDefault(require("../../util/ThemeProvider"));

var _mixins = _interopRequireDefault(require("../../util/mixins"));

var _console = require("../../util/console");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(source, true).forEach(function (key) { _defineProperty(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(source).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var baseMixins = (0, _mixins.default)(_activatable.default, _dependent.default, _detachable.default, _overlayable.default, _returnable.default, _stackable.default, _toggleable.default);
/* @vue/component */

var _default = baseMixins.extend({
  name: 'v-dialog',
  directives: {
    ClickOutside: _clickOutside.default
  },
  props: {
    dark: Boolean,
    disabled: Boolean,
    fullscreen: Boolean,
    light: Boolean,
    maxWidth: {
      type: [String, Number],
      default: 'none'
    },
    noClickAnimation: Boolean,
    origin: {
      type: String,
      default: 'center center'
    },
    persistent: Boolean,
    retainFocus: {
      type: Boolean,
      default: true
    },
    scrollable: Boolean,
    transition: {
      type: [String, Boolean],
      default: 'dialog-transition'
    },
    width: {
      type: [String, Number],
      default: 'auto'
    }
  },
  data: function data() {
    return {
      activatedBy: null,
      animate: false,
      animateTimeout: -1,
      isActive: !!this.value,
      stackMinZIndex: 200
    };
  },
  computed: {
    classes: function classes() {
      var _ref;

      return _ref = {}, _defineProperty(_ref, "v-dialog ".concat(this.contentClass).trim(), true), _defineProperty(_ref, 'v-dialog--active', this.isActive), _defineProperty(_ref, 'v-dialog--persistent', this.persistent), _defineProperty(_ref, 'v-dialog--fullscreen', this.fullscreen), _defineProperty(_ref, 'v-dialog--scrollable', this.scrollable), _defineProperty(_ref, 'v-dialog--animated', this.animate), _ref;
    },
    contentClasses: function contentClasses() {
      return {
        'v-dialog__content': true,
        'v-dialog__content--active': this.isActive
      };
    },
    hasActivator: function hasActivator() {
      return Boolean(!!this.$slots.activator || !!this.$scopedSlots.activator);
    }
  },
  watch: {
    isActive: function isActive(val) {
      if (val) {
        this.show();
        this.hideScroll();
      } else {
        this.removeOverlay();
        this.unbind();
      }
    },
    fullscreen: function fullscreen(val) {
      if (!this.isActive) return;

      if (val) {
        this.hideScroll();
        this.removeOverlay(false);
      } else {
        this.showScroll();
        this.genOverlay();
      }
    }
  },
  created: function created() {
    /* istanbul ignore next */
    if (this.$attrs.hasOwnProperty('full-width')) {
      (0, _console.removed)('full-width', this);
    }
  },
  beforeMount: function beforeMount() {
    var _this = this;

    this.$nextTick(function () {
      _this.isBooted = _this.isActive;
      _this.isActive && _this.show();
    });
  },
  beforeDestroy: function beforeDestroy() {
    if (typeof window !== 'undefined') this.unbind();
  },
  methods: {
    animateClick: function animateClick() {
      var _this2 = this;

      this.animate = false; // Needed for when clicking very fast
      // outside of the dialog

      this.$nextTick(function () {
        _this2.animate = true;
        window.clearTimeout(_this2.animateTimeout);
        _this2.animateTimeout = window.setTimeout(function () {
          return _this2.animate = false;
        }, 150);
      });
    },
    closeConditional: function closeConditional(e) {
      var target = e.target; // If the dialog content contains
      // the click event, or if the
      // dialog is not active, or if the overlay
      // is the same element as the target

      if (this._isDestroyed || !this.isActive || this.$refs.content.contains(target) || this.overlay && target && !this.overlay.$el.contains(target)) return false; // If we made it here, the click is outside
      // and is active. If persistent, and the
      // click is on the overlay, animate

      this.$emit('click:outside');

      if (this.persistent && this.overlay) {
        if (!this.noClickAnimation && (this.overlay.$el === target || this.overlay.$el.contains(target))) this.animateClick();
        return false;
      } // close dialog if !persistent, clicked outside and we're the topmost dialog.
      // Since this should only be called in a capture event (bottom up), we shouldn't need to stop propagation


      return this.activeZIndex >= this.getMaxZIndex();
    },
    hideScroll: function hideScroll() {
      if (this.fullscreen) {
        document.documentElement.classList.add('overflow-y-hidden');
      } else {
        _overlayable.default.options.methods.hideScroll.call(this);
      }
    },
    show: function show() {
      var _this3 = this;

      !this.fullscreen && !this.hideOverlay && this.genOverlay();
      this.$nextTick(function () {
        _this3.$refs.content.focus();

        _this3.bind();
      });
    },
    bind: function bind() {
      window.addEventListener('focusin', this.onFocusin);
    },
    unbind: function unbind() {
      window.removeEventListener('focusin', this.onFocusin);
    },
    onKeydown: function onKeydown(e) {
      if (e.keyCode === _helpers.keyCodes.esc && !this.getOpenDependents().length) {
        if (!this.persistent) {
          this.isActive = false;
          var activator = this.getActivator();
          this.$nextTick(function () {
            return activator && activator.focus();
          });
        } else if (!this.noClickAnimation) {
          this.animateClick();
        }
      }

      this.$emit('keydown', e);
    },
    onFocusin: function onFocusin(e) {
      if (!e || e.target === document.activeElement || !this.retainFocus) return;
      var target = e.target;

      if (!!target && // It isn't the document or the dialog body
      ![document, this.$refs.content].includes(target) && // It isn't inside the dialog body
      !this.$refs.content.contains(target) && // We're the topmost dialog
      this.activeZIndex >= this.getMaxZIndex() && // It isn't inside a dependent element (like a menu)
      !this.getOpenDependentElements().some(function (el) {
        return el.contains(target);
      }) // So we must have focused something outside the dialog and its children
      ) {
          // Find and focus the first available element inside the dialog
          var focusable = this.$refs.content.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
          focusable.length && focusable[0].focus();
        }
    }
  },
  render: function render(h) {
    var _this4 = this;

    var children = [];
    var data = {
      class: this.classes,
      ref: 'dialog',
      directives: [{
        name: 'click-outside',
        value: function value() {
          _this4.isActive = false;
        },
        args: {
          closeConditional: this.closeConditional,
          include: this.getOpenDependentElements
        }
      }, {
        name: 'show',
        value: this.isActive
      }],
      on: {
        click: function click(e) {
          e.stopPropagation();
        }
      },
      style: {}
    };

    if (!this.fullscreen) {
      data.style = {
        maxWidth: this.maxWidth === 'none' ? undefined : (0, _helpers.convertToUnit)(this.maxWidth),
        width: this.width === 'auto' ? undefined : (0, _helpers.convertToUnit)(this.width)
      };
    }

    children.push(this.genActivator());
    var dialog = h('div', data, this.showLazyContent(this.getContentSlot()));

    if (this.transition) {
      dialog = h('transition', {
        props: {
          name: this.transition,
          origin: this.origin
        }
      }, [dialog]);
    }

    children.push(h('div', {
      class: this.contentClasses,
      attrs: _objectSpread({
        role: 'document',
        tabindex: this.isActive ? 0 : undefined
      }, this.getScopeIdAttrs()),
      on: {
        keydown: this.onKeydown
      },
      style: {
        zIndex: this.activeZIndex
      },
      ref: 'content'
    }, [this.$createElement(_ThemeProvider.default, {
      props: {
        root: true,
        light: this.light,
        dark: this.dark
      }
    }, [dialog])]));
    return h('div', {
      staticClass: 'v-dialog__container',
      class: {
        'v-dialog__container--attached': this.attach === '' || this.attach === true || this.attach === 'attach'
      },
      attrs: {
        role: 'dialog'
      }
    }, children);
  }
});

exports.default = _default;
//# sourceMappingURL=VDialog.js.map