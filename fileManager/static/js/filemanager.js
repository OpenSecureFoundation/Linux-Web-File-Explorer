/* ============================================================
   filemanager.js  –  Interactions UI (sans backend)
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ══════════════════════════════════════════════════════════
    // 1. SÉLECTION DES LIGNES + ACTIVATION DE LA TOOLBAR
    // ══════════════════════════════════════════════════════════

    const tbody          = document.getElementById('fm-tbody');
    const checkAll       = document.getElementById('fm-check-all');
    const selBtns        = document.querySelectorAll('.fm-action--sel');
    const btnSelectAll   = document.getElementById('btn-select-all');
    const btnUnselectAll = document.getElementById('btn-unselect-all');

    function getCheckedRows() {
        return document.querySelectorAll('.fm-row.fm-row--selected');
    }

    function updateToolbar() {
        const count = getCheckedRows().length;
        selBtns.forEach(btn => {
            btn.classList.toggle('fm-action--active', count > 0);
        });
    }

    function toggleRow(row, force) {
        const cb  = row.querySelector('.fm-checkbox');
        const sel = force !== undefined ? force : !row.classList.contains('fm-row--selected');
        row.classList.toggle('fm-row--selected', sel);
        if (cb) cb.checked = sel;
    }

    function syncCheckAll() {
        if (!checkAll) return;
        const all = document.querySelectorAll('.fm-row');
        const sel = getCheckedRows();
        checkAll.checked       = sel.length === all.length && all.length > 0;
        checkAll.indeterminate = sel.length > 0 && sel.length < all.length;
    }

    if (tbody) {
        tbody.addEventListener('click', (e) => {
            const row = e.target.closest('.fm-row');
            if (!row) return;

            if (e.target.classList.contains('fm-checkbox')) {
                row.classList.toggle('fm-row--selected', e.target.checked);
                updateToolbar(); syncCheckAll(); return;
            }

            if (e.target.classList.contains('fm-file-link')) return;

            if (!e.ctrlKey && !e.metaKey) {
                document.querySelectorAll('.fm-row.fm-row--selected').forEach(r => toggleRow(r, false));
            }
            toggleRow(row);
            updateToolbar(); syncCheckAll();
        });
    }

    if (checkAll) {
        checkAll.addEventListener('change', () => {
            document.querySelectorAll('.fm-row').forEach(r => toggleRow(r, checkAll.checked));
            updateToolbar();
        });
    }

    if (btnSelectAll) {
        btnSelectAll.addEventListener('click', e => {
            e.preventDefault();
            document.querySelectorAll('.fm-row').forEach(r => toggleRow(r, true));
            if (checkAll) checkAll.checked = true;
            updateToolbar();
        });
    }

    if (btnUnselectAll) {
        btnUnselectAll.addEventListener('click', e => {
            e.preventDefault();
            document.querySelectorAll('.fm-row').forEach(r => toggleRow(r, false));
            if (checkAll) { checkAll.checked = false; checkAll.indeterminate = false; }
            updateToolbar();
        });
    }

    // ══════════════════════════════════════════════════════════
    // 2. ARBORESCENCE SIDEBAR
    // ══════════════════════════════════════════════════════════

    const tree = document.getElementById('fm-sidebar-tree');

    if (tree) {
        tree.addEventListener('click', e => {
            const toggle = e.target.closest('.fm-tree-toggle');
            const row    = e.target.closest('.fm-tree-row');

            if (toggle) {
                e.stopPropagation();
                const node     = toggle.closest('.fm-tree-node');
                const children = node && node.querySelector(':scope > .fm-tree-children');
                if (!children) return;
                const isOpen = !children.classList.contains('fm-tree-children--collapsed');
                children.classList.toggle('fm-tree-children--collapsed', isOpen);
                toggle.classList.toggle('fm-tree-toggle--open',   !isOpen);
                toggle.classList.toggle('fm-tree-toggle--closed',  isOpen);
                return;
            }

            if (row) {
                tree.querySelectorAll('.fm-tree-row--active').forEach(r => r.classList.remove('fm-tree-row--active'));
                row.classList.add('fm-tree-row--active');
            }
        });
    }

    const collapseBtn = document.getElementById('fm-collapse-all');
    if (collapseBtn && tree) {
        collapseBtn.addEventListener('click', () => {
            tree.querySelectorAll('.fm-tree-children').forEach(c => c.classList.add('fm-tree-children--collapsed'));
            tree.querySelectorAll('.fm-tree-toggle').forEach(t => {
                t.classList.remove('fm-tree-toggle--open');
                t.classList.add('fm-tree-toggle--closed');
            });
            // Rouvrir root
            const rootChildren = tree.querySelector(':scope > .fm-tree-node > .fm-tree-children');
            if (rootChildren) {
                rootChildren.classList.remove('fm-tree-children--collapsed');
                const rt = tree.querySelector('.fm-tree-row--root .fm-tree-toggle');
                if (rt) { rt.classList.add('fm-tree-toggle--open'); rt.classList.remove('fm-tree-toggle--closed'); }
            }
        });
    }

    updateToolbar();
});