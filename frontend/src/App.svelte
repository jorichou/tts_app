<script>
  import { onDestroy } from "svelte";
  import { synthesizeAudio } from "./lib/api.js";

  let selectedFile = null;
  let isLoading = false;
  let errorMessage = "";
  let audioUrl = "";
  let downloadName = "voice.wav";

  function setFile(file) {
    errorMessage = "";

    if (!file) {
      selectedFile = null;
      return;
    }

    if (!file.name.toLowerCase().endsWith(".txt")) {
      selectedFile = null;
      errorMessage = ".txt ファイルを選択してください。";
      return;
    }

    selectedFile = file;
  }

  function handleFileChange(event) {
    const [file] = event.currentTarget.files ?? [];
    setFile(file);
  }

  function resetAudioUrl() {
    if (audioUrl) {
      URL.revokeObjectURL(audioUrl);
      audioUrl = "";
    }
  }

  async function handleSubmit() {
    if (!selectedFile || isLoading) {
      return;
    }

    isLoading = true;
    errorMessage = "";
    resetAudioUrl();

    try {
      const audioBlob = await synthesizeAudio(selectedFile);
      audioUrl = URL.createObjectURL(audioBlob);
      downloadName = selectedFile.name.replace(/\.txt$/i, "") || "voice";
      downloadName = `${downloadName}.wav`;
    } catch (error) {
      errorMessage =
        error instanceof Error
          ? error.message
          : "音声生成に失敗しました。VOICEVOX とバックエンドの起動状態を確認してください。";
    } finally {
      isLoading = false;
    }
  }

  onDestroy(() => {
    resetAudioUrl();
  });
</script>

<svelte:head>
  <title>テキスト読み上げ</title>
</svelte:head>

<main>
    <h1>テキスト読み上げ</h1>
    <p class="description">.txtファイルをアップロードして、VOICEVOX　で音声生成します。</p>
    <label for="fileInput"　class="upload">
        <span>テキストファイルを選択</span>
        <input type="file" accept=".txt,text/plain" on:change={handleFileChange} />
    </label>

    <p class="file-name">
        {#if selectedFile}
            選択中: {selectedFile.name}
        {:else}
            まだファイルが選択されていません
        {/if}
    </p>
    
    <button class="primary-button" on:click={handleSubmit} disabled={!selectedFile || isLoading}>
        {#if isLoading}
            生成中...
        {:else}
            音声を生成
        {/if}
    </button>

    {#if errorMessage}
        <p class="message error">{errorMessage}</p>
    {/if}

    {#if audioUrl}
        <div class="result">
            <audio controls src={audioUrl} class="player">
                お使いのブラウザは音声再生に対応していません。
            </audio>

            <a class="download-link" href={audioUrl} download={downloadName}>
                WAV をダウンロード
            </a>
        </div>
    {/if}
</main>