import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.ppj.fuwuqi',
  appName: '服务器',
  webDir: 'www',
  server: {
    url: 'http://192.168.0.171:8000',
    cleartext: true,
  },
  ios: {
    contentInset: 'never',
  },
};

export default config;
