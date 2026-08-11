document.addEventListener('DOMContentLoaded', () => {
  // State
  let selectedFile = null;

  // DOM Elements - Views
  const viewHome = document.getElementById('view-home');
  const viewUpload = document.getElementById('view-upload');
  const viewResults = document.getElementById('view-results');

  // DOM Elements - Home Buttons
  const cardCompress = document.getElementById('card-compress');
  const cardGrayscale = document.getElementById('card-grayscale');
  const navLogo = document.getElementById('nav-logo');
  const btnBackHome = document.getElementById('btn-back-home');
  const btnCompressAnother = document.getElementById('btn-compress-another');

  // DOM Elements - Workspace & Dropzone
  const dropzone = document.getElementById('dropzone');
  const fileInput = document.getElementById('file-input');
  const dropzonePrompt = document.getElementById('dropzone-prompt');
  const filePreview = document.getElementById('file-preview');
  const previewImg = document.getElementById('preview-img');
  const previewFilename = document.getElementById('preview-filename');
  const previewFilesize = document.getElementById('preview-filesize');
  const btnRemoveFile = document.getElementById('btn-remove-file');

  // DOM Elements - Controls
  const inputTargetKb = document.getElementById('input-target-kb');
  const chkGrayscale = document.getElementById('chk-grayscale');
  const btnCompressSubmit = document.getElementById('btn-compress-submit');
  const btnText = document.getElementById('btn-text');
  const btnSpinner = document.getElementById('btn-spinner');
  const presetBtns = document.querySelectorAll('.preset-btn');

  // DOM Elements - Results
  const imgOriginal = document.getElementById('img-original');
  const imgCompressed = document.getElementById('img-compressed');
  const statOrigSize = document.getElementById('stat-orig-size');
  const statCompSize = document.getElementById('stat-comp-size');
  const statReduction = document.getElementById('stat-reduction');
  const statKUsed = document.getElementById('stat-k-used');
  const swatchesGrid = document.getElementById('swatches-grid');
  const btnDownload = document.getElementById('btn-download');

  // DOM Elements - Comparison Slider
  const compContainer = document.getElementById('comparison-container');
  const compOverlay = document.getElementById('comp-overlay');
  const compHandle = document.getElementById('comp-handle');

  // --- NAVIGATION & VIEW SWITCHING ---
  function showView(viewName) {
    [viewHome, viewUpload, viewResults].forEach(v => {
      v.classList.remove('active');
      v.classList.add('hidden');
    });

    if (viewName === 'home') {
      viewHome.classList.remove('hidden');
      viewHome.classList.add('active');
    } else if (viewName === 'upload') {
      viewUpload.classList.remove('hidden');
      viewUpload.classList.add('active');
    } else if (viewName === 'results') {
      viewResults.classList.remove('hidden');
      viewResults.classList.add('active');
      initComparisonSlider();
    }
  }

  navLogo.addEventListener('click', () => showView('home'));
  btnBackHome.addEventListener('click', () => showView('home'));
  btnCompressAnother.addEventListener('click', () => showView('upload'));

  cardCompress.addEventListener('click', () => {
    chkGrayscale.checked = false;
    showView('upload');
  });

  cardGrayscale.addEventListener('click', () => {
    chkGrayscale.checked = true;
    showView('upload');
  });

  // --- PRESET BUTTONS ---
  presetBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      presetBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      inputTargetKb.value = btn.getAttribute('data-size');
    });
  });

  inputTargetKb.addEventListener('input', () => {
    presetBtns.forEach(b => b.classList.remove('active'));
  });

  // --- FILE DROPZONE HANDLERS ---
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, preventDefaults, false);
  });

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, () => dropzone.classList.add('dragover'), false);
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, () => dropzone.classList.remove('dragover'), false);
  });

  dropzone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length > 0) {
      handleFileSelect(files[0]);
    }
  });

  fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
      handleFileSelect(e.target.files[0]);
    }
  });

  function handleFileSelect(file) {
    if (!file.type.startsWith('image/')) {
      alert('Please upload a valid image file (PNG, JPG, WEBP, BMP).');
      return;
    }

    selectedFile = file;
    const reader = new FileReader();

    reader.onload = (e) => {
      previewImg.src = e.target.result;
      previewFilename.textContent = file.name;
      previewFilesize.textContent = formatBytes(file.size);

      dropzonePrompt.classList.add('hidden');
      filePreview.classList.remove('hidden');
      btnCompressSubmit.disabled = false;
    };

    reader.readAsDataURL(file);
  }

  btnRemoveFile.addEventListener('click', (e) => {
    e.stopPropagation();
    selectedFile = null;
    fileInput.value = '';
    previewImg.src = '';
    dropzonePrompt.classList.remove('hidden');
    filePreview.classList.add('hidden');
    btnCompressSubmit.disabled = true;
  });

  function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  // --- SUBMIT TO FASTAPI BACKEND ---
  btnCompressSubmit.addEventListener('click', async () => {
    if (!selectedFile) return;

    btnCompressSubmit.disabled = true;
    btnText.textContent = 'Compressing Image...';
    btnSpinner.classList.remove('hidden');

    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('mode', 'target_size');
    formData.append('target_kb', inputTargetKb.value);
    formData.append('is_grayscale', chkGrayscale.checked);

    try {
      const response = await fetch('/api/compress', {
        method: 'POST',
        body: formData
      });

      const data = await response.json();

      if (!response.ok || !data.success) {
        throw new Error(data.detail || 'Compression failed');
      }

      renderResults(data);
      showView('results');

    } catch (err) {
      alert('Error compressing image: ' + err.message);
    } finally {
      btnCompressSubmit.disabled = false;
      btnText.textContent = 'Compress to Target Size';
      btnSpinner.classList.add('hidden');
    }
  });

  // --- RENDER RESULTS & SWATCHES ---
  function renderResults(data) {
    imgOriginal.src = data.original_image;
    imgCompressed.src = data.compressed_image;

    statOrigSize.textContent = data.original_size_kb + ' KB';
    statCompSize.textContent = data.final_size_kb + ' KB';
    statReduction.textContent = '-' + data.reduction_percent + '%';
    statKUsed.textContent = data.final_k;

    btnDownload.href = data.compressed_image;
    btnDownload.download = `compressed_${data.final_size_kb}KB_${data.filename}`;

    // Render Swatches
    swatchesGrid.innerHTML = '';
    if (data.hex_colors && data.hex_colors.length > 0) {
      data.hex_colors.forEach(hex => {
        const card = document.createElement('div');
        card.className = 'swatch-card';
        card.innerHTML = `
          <div class="swatch-box" style="background-color: ${hex};"></div>
          <span class="swatch-hex">${hex}</span>
        `;
        card.addEventListener('click', () => {
          navigator.clipboard.writeText(hex);
          const hexLabel = card.querySelector('.swatch-hex');
          const origText = hexLabel.textContent;
          hexLabel.textContent = 'Copied!';
          setTimeout(() => hexLabel.textContent = origText, 1200);
        });
        swatchesGrid.appendChild(card);
      });
    }
  }

  // --- COMPARISON SPLIT SLIDER ---
  let isDragging = false;

  function initComparisonSlider() {
    updateSliderPosition(50);
  }

  function updateSliderPosition(percent) {
    percent = Math.max(0, Math.min(100, percent));
    compOverlay.style.width = percent + '%';
    compHandle.style.left = percent + '%';
  }

  function getPercentFromEvent(e) {
    const rect = compContainer.getBoundingClientRect();
    const x = (e.clientX || (e.touches && e.touches[0].clientX)) - rect.left;
    return (x / rect.width) * 100;
  }

  compContainer.addEventListener('mousedown', (e) => {
    isDragging = true;
    updateSliderPosition(getPercentFromEvent(e));
  });

  window.addEventListener('mouseup', () => isDragging = false);

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    updateSliderPosition(getPercentFromEvent(e));
  });

  compContainer.addEventListener('touchstart', (e) => {
    isDragging = true;
    updateSliderPosition(getPercentFromEvent(e));
  });

  window.addEventListener('touchend', () => isDragging = false);

  window.addEventListener('touchmove', (e) => {
    if (!isDragging) return;
    updateSliderPosition(getPercentFromEvent(e));
  });
});
